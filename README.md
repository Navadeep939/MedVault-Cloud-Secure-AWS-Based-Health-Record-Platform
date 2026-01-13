<h1 align="center" style="font-size: 4em;">🛡️ MedVault Cloud - Secure PHR Platform</h1>

MedVault Cloud is a secure, HIPAA-compliant Personal Health Record (PHR) system architecture designed for the AWS Cloud. It demonstrates a Zero-Trust security model, utilizing Infrastructure as Code (Terraform) to provision a 3-tier isolated network, and integrates Generative AI for health insights and architectural analysis.

<h2 align="center" style="font-size: 3em;">🏗️ System Architecture</h2>

This project implements a standard 3-Tier Web Architecture optimized for security:

Presentation Tier: Python Flask Web Application (EC2).

Logic Tier: AI Orchestration & Business Logic (Private Subnet).

Data Tier: Amazon RDS (PostgreSQL) & S3 (KMS Encrypted) for records.

<h3 align="center" style="font-size: 2em;">Architecture Diagram</h3>
<img width="1024" height="474" alt="3TierArchitecture drawio-3-1024x474" src="https://github.com/user-attachments/assets/a839b8d4-ce57-4792-8708-5a0b06bb06a9" />

                      High-Level Architecture Diagram
                     
<h3 align="center" style="font-size: 2em;">Key Security Controls</h3>

Network Isolation: Database and Logic tiers reside in Private Subnets.

Encryption at Rest: All S3 objects are encrypted using AWS KMS (AES-256).

Encryption in Transit: TLS 1.3 enforced for all connections.

IAM Least Privilege: EC2 instances use restricted IAM Roles to access S3.

WAF Integration: Simulated protection against SQL Injection and XSS.

<h3 align="center" style="font-size: 2em;">Architecture Diagram</h3>

![1-Architecture1853](https://github.com/user-attachments/assets/21eeecad-33f2-4796-bbfd-710e4cde1583)

                       Security-Focused Architecture Diagram
                     
<h2 align="center" style="font-size: 3em;">✨ Key Features</h2>

<h3 align="center" style="font-size: 2em;">👨‍💻 Admin & Architect Dashboard</h3>

Infrastructure Visualization: Interactive map of AWS components.

SOC Dashboard: Live threat feed (WAF logs) and FinOps cost estimation.

Deployment Lab: Simulate Terraform init/apply workflows.

Chaos Engineering: Trigger simulated EC2 failures to test Auto Scaling resilience.

<img width="1710" height="988" alt="Screenshot 2026-01-13 at 7 57 37 AM" src="https://github.com/user-attachments/assets/110d9609-fa27-4fb2-86e3-0accb2b789d5" />



<h3 align="center" style="font-size: 2em;">👩‍⚕️ Patient Health Portal</h3>

Secure Access: Role-based authentication (simulated AWS Cognito).

Health Vitals: Real-time visualization of Heart Rate, BP, and SpO2.

Encrypted Vault: Upload and store medical records (PDF/Imaging) securely to S3.

MedVault AI Assistant: Context-aware chatbot for interpreting medical data.

<img width="1687" height="982" alt="Screenshot 2026-01-13 at 8 00 50 AM" src="https://github.com/user-attachments/assets/d86b8422-8dd9-4582-a0d3-9c26aa6531bc" />


<h2 align="center" style="font-size: 3em;">🛠️ Technology Stack</h2>

Backend: Python (Flask), Boto3 (AWS SDK)

Infrastructure: HashiCorp Terraform

Frontend: HTML5, Tailwind CSS, JavaScript (Vanilla)

AI Engine: Medvault API (via MedVault AI module)

tabase: PostgreSQL (AWS RDS)
<img width="1710" height="987" alt="Screenshot 2026-01-13 at 8 02 19 AM" src="https://github.com/user-attachments/assets/21b4ebaa-54b7-4f5f-9d4f-0c12e30ab352" />
<img width="1704" height="986" alt="Screenshot 2026-01-13 at 8 02 44 AM" src="https://github.com/user-attachments/assets/969a17cf-3e1d-4399-a5da-509da945f3b5" />

<img width="1705" height="982" alt="Screenshot 2026-01-13 at 8 03 17 AM" src="https://github.com/user-attachments/assets/6f846121-3244-4c92-b847-2d40536107e0" />

<h3 align="center" style="font-size: 2em;">Installation</h3>

Clone the Repository

git clone [https://github.com/yourusername/medvault-cloud.git](https://github.com/yourusername/medvault-cloud.git)
cd medvault-cloud


Set Up a Virtual Environment (Recommended)

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate


Install Dependencies

pip install -r requirements.txt


Configure Environment Variables

Create a .env file in the root directory to store secrets securely:

# Flask Security
SECRET_KEY=dev-secret-key-change-in-prod

# AWS Configuration (Simulation Context)
S3_BUCKET_NAME=medvault-patient-records
KMS_KEY_ID=alias/medvault-key
AWS_REGION=us-east-1

# AI Integration
MEDVAULT_AI_KEY=your_google_gemini_api_key


Run the Application

python app.py


Open your browser and navigate to http://localhost:5000.

<h2 align="center" style="font-size: 3em;">📂 Project Structure</h2>

medvault-cloud/
├── app.py                  # Main Flask Application Entry Point
├── config.py               # Security & AWS Configuration
├── requirements.txt        # Python Dependencies
├── modules/                # Core Logic Modules
│   ├── ai_chat.py          # AI Chatbot Engine (Gemini Integration)
│   ├── chaos.py            # Chaos Engineering Simulator
│   ├── terraform_runner.py # IaC Simulation Logic
│   ├── networking/         # Terraform VPC Module
│   ├── compute/            # Terraform EC2 Module
│   ├── storage/            # Terraform S3 Module
│   ├── database/           # Terraform RDS Module
│   └── iam/                # Terraform IAM Policies
└── templates/              # HTML Frontend Templates
    └── login.html          # Authentication UI
    └── admin_dashboard.html # Admin Ops Center
    └── patient_portal.html  # Patient Interface

