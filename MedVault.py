import os
import boto3
import random
import time
import logging
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from config import Config

# Import Logic Modules
from modules.terraform_runner import TerraformRunner
from modules.chaos import ChaosEngine
from modules.ai_chat import AIChatEngine

# --- LOGGING SETUP ---
# This makes debugging easier by printing actions to the terminal
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("MedVaultApp")

app = Flask(__name__)
app.config.from_object(Config)

# Mock Database
users = {
    "admin@hospital.org": {"role": "admin", "password": "password123"},
    "alice@patient.com": {"role": "patient", "password": "password123"}
}

# --- MIDDLEWARE ---
@app.after_request
def add_security_headers(response):
    for header, value in app.config['SECURITY_HEADERS'].items():
        response.headers[header] = value
    return response

# --- PAGE ROUTES ---
@app.route('/')
def index():
    logger.info(f"Index accessed. Session: {session.get('user')}")
    if 'user' in session:
        return redirect(url_for(session['role'] + '_dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    logger.debug(f"Login attempt for email: {email}")
    
    user = users.get(email)
    if user and user['password'] == password:
        session['user'] = email
        session['role'] = user['role']
        logger.info(f"Login successful for {email} as {user['role']}")
        return redirect(url_for(user['role'] + '_dashboard'))
    
    logger.warning(f"Failed login attempt for {email}")
    return render_template('login.html', error="Invalid Credentials")

@app.route('/logout')
def logout():
    logger.info(f"User {session.get('user')} logged out.")
    session.clear()
    return redirect(url_for('index'))

@app.route('/admin/dashboard')
def admin_dashboard():
    if session.get('role') != 'admin':
        logger.warning("Unauthorized access attempt to Admin Dashboard")
        return redirect(url_for('index'))
    return render_template('admin_dashboard.html')

@app.route('/patient/portal')
def patient_dashboard():
    if session.get('role') != 'patient':
        logger.warning("Unauthorized access attempt to Patient Portal")
        return redirect(url_for('index'))
    
    # Simulate fetching live vitals
    vitals = {
        "hr": random.randint(68, 76),
        "bp": f"{random.randint(115, 125)}/{random.randint(75, 82)}",
        "spo2": random.randint(97, 99)
    }
    logger.debug(f"Fetched vitals for patient: {vitals}")
    return render_template('patient_portal.html', vitals=vitals)

# --- API ROUTES ---

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'user' not in session: return jsonify({"error": "Unauthorized"}), 401
    
    if 'file' not in request.files: return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    
    if file.filename == '': return jsonify({"error": "No selected file"}), 400

    logger.info(f"Starting upload for file: {file.filename} by {session['user']}")
    s3 = boto3.client('s3', region_name=app.config['AWS_REGION'])
    
    try:
        s3.upload_fileobj(
            file,
            app.config['S3_BUCKET_NAME'],
            f"{session['user']}/{file.filename}",
            ExtraArgs={
                'ServerSideEncryption': 'aws:kms',
                'SSEKMSKeyId': app.config['KMS_KEY_ID']
            }
        )
        logger.info("Upload successful.")
        return jsonify({"message": "File encrypted & uploaded to S3 successfully."})
    except Exception as e:
        logger.error(f"Upload failed: {str(e)}", exc_info=True)
        return jsonify({"error": f"Upload failed: {str(e)}"}), 500

@app.route('/api/terraform/<command>', methods=['POST'])
def run_terraform(command):
    if session.get('role') != 'admin': return jsonify({"error": "Unauthorized"}), 403

    logger.info(f"Running Terraform command: {command}")
    runner = TerraformRunner()
    if command == 'init':
        return jsonify(runner.init())
    elif command == 'apply':
        return jsonify(runner.apply())
    
    logger.error(f"Invalid Terraform command: {command}")
    return jsonify({"error": "Invalid command"}), 400

@app.route('/api/chaos/<action>', methods=['POST'])
def trigger_chaos(action):
    if session.get('role') != 'admin': return jsonify({"error": "Unauthorized"}), 403
    
    logger.info(f"Triggering Chaos action: {action}")
    chaos = ChaosEngine()
    if action == 'ec2-fail':
        return jsonify(chaos.simulate_ec2_failure())
    elif action == 'sql-inject':
        return jsonify(chaos.simulate_sql_injection())
    
    logger.error(f"Unknown chaos action: {action}")
    return jsonify({"error": "Unknown chaos action"}), 400

@app.route('/api/ai/chat', methods=['POST'])
def chat_ai():
    if 'user' not in session: return jsonify({"error": "Unauthorized"}), 401
    
    data = request.json
    user_message = data.get('message')
    logger.debug(f"AI Chat Request from {session['user']}: {user_message}")
    
    context = None
    if session['role'] == 'patient':
        context = "HR: 72bpm, BP: 118/78, Allergies: Penicillin"
    
    ai = AIChatEngine()
    response = ai.generate_response(user_message, role=session['role'], context_data=context)
    
    logger.debug(f"AI Response generated: {response[:50]}...")
    return jsonify({"response": response})

if __name__ == '__main__':
    print("🚀 MedVault Cloud starting in DEBUG mode...")
    print(f"📂 KMS Key ID: {app.config['KMS_KEY_ID']}")
    print(f"📂 S3 Bucket: {app.config['S3_BUCKET_NAME']}")
    app.run(host='0.0.0.0', port=5000, debug=True)
