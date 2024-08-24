resource "aws_instance" "app_server" {
  ami           = var.instance_ami_aws
  instance_type = var.instance_type_aws
  key_name      = aws_key_pair.aws_key_pair.key_name

  associate_public_ip_address = true

  vpc_security_group_ids = [aws_security_group.alb.id]

  subnet_id = module.vpc.public_subnets[0]

  iam_instance_profile = aws_iam_instance_profile.ec2_access_ecr_profile.name

  tags = {
    Name        = "${var.project-name}-ec2"
    Project     = "${var.project-name}"
    Terraform   = "true"
    Environment = "${var.project-environment}"
  }

  depends_on = [aws_key_pair.aws_key_pair, aws_iam_instance_profile.ec2_access_ecr_profile]
}
