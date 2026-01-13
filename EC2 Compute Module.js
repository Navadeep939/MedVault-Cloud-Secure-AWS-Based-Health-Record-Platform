resource "aws_security_group" "web_sg" {
  name        = "medvault-web-sg"
  description = "Allow inbound HTTP/HTTPS"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "app_server" {
  ami                  = "ami-0c7217cdde317cfec" # Ubuntu 22.04
  instance_type        = "t2.micro"
  subnet_id            = var.public_subnet_id
  iam_instance_profile = var.iam_instance_profile
  vpc_security_group_ids = [aws_security_group.web_sg.id]
  
  tags = { Name = "MedVault-App-Server" }
}
