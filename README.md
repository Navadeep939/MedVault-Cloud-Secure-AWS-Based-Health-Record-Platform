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

<h3 align="center" style="font-size: 2em;">👩‍⚕️ Patient Health Portal</h3>

Secure Access: Role-based authentication (simulated AWS Cognito).

Health Vitals: Real-time visualization of Heart Rate, BP, and SpO2.

Encrypted Vault: Upload and store medical records (PDF/Imaging) securely to S3.

MedVault AI Assistant: Context-aware chatbot for interpreting medical data.

<h2 align="center" style="font-size: 3em;">🛠️ Technology Stack</h2>

Backend: Python (Flask), Boto3 (AWS SDK)

Infrastructure: HashiCorp Terraform

Frontend: HTML5, Tailwind CSS, JavaScript (Vanilla)

AI Engine: Google Gemini API (via MedVault AI module)

Database: PostgreSQL (AWS RDS)

Storage: AWS S3 + KMS

