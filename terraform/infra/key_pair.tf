resource "aws_key_pair" "aws_key_pair" {
  key_name   = "${var.project-name}-${var.project-environment}-ssh_id"
  public_key = var.ssh_key_public

  tags = {
    Name        = "${var.project-name}-ssh-key-pair"
    Project     = "${var.project-name}"
    Terraform   = "true"
    Environment = "${var.project-environment}"
  }
}
