output "IP" {
  value      = aws_eip.project_lb.public_ip
  depends_on = [aws_eip.project_lb]
}

output "ecr_repository_url" {
  value = aws_ecr_repository.repository.repository_url
}
