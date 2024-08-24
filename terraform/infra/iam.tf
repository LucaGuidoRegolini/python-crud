resource "aws_iam_role" "ec2_access_ecr" {
  name = "${var.project-name}-${var.project-environment}-access_ecr_ec2"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Effect = "Allow",
      Principal = {
        Service = [
          "ec2.amazonaws.com"

        ]
      }
    }]
  })
}
resource "aws_iam_role_policy" "ecs_ecr_policy_ec2" {
  name = "${var.project-name}-${var.project-environment}-ecs_ecr_policy_ec2"
  role = aws_iam_role.ec2_access_ecr.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "ecr:*"
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}

resource "aws_iam_role_policy" "ecs_logs_policy_ec2" {
  name = "${var.project-name}-${var.project-environment}-ecs_ecr_policy_ec2"
  role = aws_iam_role.ec2_access_ecr.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "cloudtrail:LookupEvents",
          "logs:CreateLogStream",
          "logs:PutLogEvents",
          "logs:CreateLogGroup",
          "logs:DescribeLogGroups",
          "logs:DescribeLogStreams"
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}

resource "aws_iam_instance_profile" "ec2_access_ecr_profile" {
  name = "${var.project-name}-${var.project-environment}-access_ecr_ec2_profile"

  role = aws_iam_role.ec2_access_ecr.name

  tags = {
    Name        = "${var.project-name}-ec2-access-ecr-profile"
    Project     = "${var.project-name}"
    Terraform   = "true"
    Environment = "${var.project-environment}"
  }
}
