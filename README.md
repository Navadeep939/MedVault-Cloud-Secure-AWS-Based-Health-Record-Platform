#🛡️ MedVault Cloud - Secure PHR Platform

MedVault Cloud is a secure, HIPAA-compliant Personal Health Record (PHR) system architecture designed for the AWS Cloud. It demonstrates a Zero-Trust security model, utilizing Infrastructure as Code (Terraform) to provision a 3-tier isolated network, and integrates Generative AI for health insights and architectural analysis.

#🏗️ System Architecture

This project implements a standard 3-Tier Web Architecture optimized for security:

Presentation Tier: Python Flask Web Application (EC2).

Logic Tier: AI Orchestration & Business Logic (Private Subnet).

Data Tier: Amazon RDS (PostgreSQL) & S3 (KMS Encrypted) for records.

Key Security Controls

Network Isolation: Database and Logic tiers reside in Private Subnets.

Encryption at Rest: All S3 objects are encrypted using AWS KMS (AES-256).

Encryption in Transit: TLS 1.3 enforced for all connections.

IAM Least Privilege: EC2 instances use restricted IAM Roles to access S3.

WAF Integration: Simulated protection against SQL Injection and XSS.

#✨ Key Features

👨‍💻 Admin & Architect Dashboard

Infrastructure Visualization: Interactive map of AWS components.

SOC Dashboard: Live threat feed (WAF logs) and FinOps cost estimation.

Deployment Lab: Simulate Terraform init/apply workflows.

Chaos Engineering: Trigger simulated EC2 failures to test Auto Scaling resilience.

#👩‍⚕️ Patient Health Portal

Secure Access: Role-based authentication (simulated AWS Cognito).

Health Vitals: Real-time visualization of Heart Rate, BP, and SpO2.

Encrypted Vault: Upload and store medical records (PDF/Imaging) securely to S3.

MedVault AI Assistant: Context-aware chatbot for interpreting medical data.

$🛠️ Technology Stack

Backend: Python (Flask), Boto3 (AWS SDK)

Infrastructure: HashiCorp Terraform

Frontend: HTML5, Tailwind CSS, JavaScript (Vanilla)

AI Engine: Google Gemini API (via MedVault AI module)

Database: PostgreSQL (AWS RDS)

Storage: AWS S3 + KMS

#🚀 Getting Started

Prerequisites

Python 3.9+

Terraform installed (for infrastructure provisioning)

AWS CLI configured with appropriate credentials
