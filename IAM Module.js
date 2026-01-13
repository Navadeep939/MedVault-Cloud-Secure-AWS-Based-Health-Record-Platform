resource "aws_iam_role" "ec2_s3_role" {
  name = "MedVault_EC2_S3_Access"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "ec2.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy" "s3_access" {
  name = "S3_Encryption_Access"
  role = aws_iam_role.ec2_s3_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = ["s3:PutObject", "s3:GetObject", "kms:GenerateDataKey"]
      Resource = ["arn:aws:s3:::medvault-patient-records/*"]
    }]
  })
}
