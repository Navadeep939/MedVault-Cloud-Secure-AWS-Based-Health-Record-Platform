import os
import requests
import json

class AIChatEngine:
    def __init__(self, api_key=None):
        # Use environment variable if not passed explicitly
        self.api_key = api_key or os.environ.get('MEDVAULT_AI_KEY')
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key={self.api_key}"

    def get_persona_prompt(self, role, context_data=None):
        """
        Generates the system prompt based on the user's role.
        """
        if role == 'admin':
            base = (
                "You are the Lead Cloud Architect for MedVault Cloud. "
                "Tech Stack: AWS, Terraform, Python (Flask), RDS (PostgreSQL), S3 (SSE-KMS AES-256). "
                "Security: Zero-Trust IAM, Network Isolation (Private Subnets). "
                "Answer questions about infrastructure, security logs, and compliance."
            )
            if context_data:
                base += f"\n[Live System Context]\n{context_data}"
            return base
            
        elif role == 'patient':
            base = (
                "You are Dr. MedVault, a helpful AI Health Assistant for the Patient Portal. "
                "The patient is Alice Freeman (ID: PHR-8821). "
                "Speak in a reassuring, professional medical tone. "
                "Interpret vitals and medical records clearly."
            )
            if context_data:
                base += f"\n[Patient Vitals Context]\n{context_data}"
            return base
            
        return "You are a helpful assistant."

    def generate_response(self, user_message, role='patient', context_data=None):
        """
        Sends the message and system prompt to the AI model.
        """
        if not self.api_key:
            return "Simulation Mode: AI API Key not configured."

        system_instruction = self.get_persona_prompt(role, context_data)

        payload = {
            "contents": [{
                "role": "user",
                "parts": [{"text": user_message}]
            }],
            "systemInstruction": {
                "parts": [{"text": system_instruction}]
            }
        }

        try:
            response = requests.post(
                self.api_url,
                headers={'Content-Type': 'application/json'},
                data=json.dumps(payload),
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', "I couldn't generate a response.")
            else:
                return f"Error: AI Service unavailable (Status {response.status_code})"
                
        except Exception as e:
            return f"System Error: {str(e)}"

# Example Usage within app.py:
# ai = AIChatEngine()
# response = ai.generate_response("How is my heart rate?", role="patient", context_data="HR: 72bpm")
