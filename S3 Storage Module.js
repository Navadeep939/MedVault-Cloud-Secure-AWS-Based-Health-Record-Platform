resource "aws_kms_key" "medvault_key" {
  description             = "KMS key for PHR encryption"
  deletion_window_in_days = 10
}

resource "aws_s3_bucket" "phr_bucket" {
  bucket = "medvault-patient-records"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "enc" {
  bucket = aws_s3_bucket.phr_bucket.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.medvault_key.arn
    }
  }
}

resource "aws_s3_bucket_public_access_block" "block_public" {
  bucket = aws_s3_bucket.phr_bucket.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
