resource "aws_eip" "project_lb" {
  instance = aws_instance.app_server.id
  domain   = "vpc"

  depends_on = [aws_instance.app_server]

  tags = {
    Name        = "${var.project-name}-ecr"
    Project     = "${var.project-name}"
    Terraform   = "true"
    Environment = "${var.project-environment}"
  }
}


