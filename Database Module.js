resource "aws_db_subnet_group" "phr_db_subnet" {
  name       = "phr_db_subnet_group"
  subnet_ids = var.private_subnet_ids
}

resource "aws_db_instance" "default" {
  allocated_storage      = 20
  db_name                = "phrdb"
  engine                 = "postgres"
  engine_version         = "16.3"
  instance_class         = "db.t3.micro"
  username               = "phradmin"
  password               = var.db_password
  db_subnet_group_name   = aws_db_subnet_group.phr_db_subnet.name
  publicly_accessible    = false
  skip_final_snapshot    = true
}
