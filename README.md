<h1 align="center" style="font-size: 4em;">🛡️ MedVault Cloud - Secure PHR Platform</h1>

MedVault Cloud is a secure, HIPAA-compliant Personal Health Record (PHR) system architecture designed for the AWS Cloud. It demonstrates a Zero-Trust security model, utilizing Infrastructure as Code (Terraform) to provision a 3-tier isolated network, and integrates Generative AI for health insights and architectural analysis.

<h2 align="center" style="font-size: 3em;">🏗️ System Architecture</h2>

This project implements a standard 3-Tier Web Architecture optimized for security:

Presentation Tier: Python Flask Web Application (EC2).

Logic Tier: AI Orchestration & Business Logic (Private Subnet).

Data Tier: Amazon RDS (PostgreSQL) & S3 (KMS Encrypted) for records.

<h3 align="center" style="font-size: 2em;">Architecture Diagram</h3>
