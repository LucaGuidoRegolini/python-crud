resource "aws_ecr_repository" "repository" {
  name = "${var.project-name}-ecr"
  tags = {
    Name        = "${var.project-name}-ecr"
    Project     = "${var.project-name}"
    Terraform   = "true"
    Environment = "${var.project-environment}"
  }
}

resource "docker_image" "app_image" {
  name = "app_image"

  build {
    context    = "../../../"
    dockerfile = "Dockerfile"
    tag = [
      "${aws_ecr_repository.repository.repository_url}:latest"
    ]
    build_args = {
      DATABASE_URL = var.database_url
      JWT_SECRET   = var.jwt_secret
    }
  }

  triggers = {
    dir_sha1 = sha1(join("", [for f in fileset(path.module, "../../../src/*") : filesha1(f)]))
  }

}

resource "random_id" "build_id" {
  byte_length = 8
}

resource "null_resource" "push_to_ecr" {
  provisioner "local-exec" {
    command = <<EOT
    $(aws ecr get-login-password --region ${var.region} | docker login --username AWS --password-stdin ${aws_ecr_repository.repository.repository_url})
    docker push ${aws_ecr_repository.repository.repository_url}:latest
    EOT
  }

  depends_on = [aws_ecr_repository.repository, docker_image.app_image]

  triggers = {
    force_rebuild = random_id.build_id.hex
  }
}
