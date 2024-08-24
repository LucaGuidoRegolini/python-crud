terraform {
  backend "s3" {
    bucket = "terraform-python-crud-project"
    key    = "dev/terraform.tfstate"
    region = "us-east-1"
  }
}