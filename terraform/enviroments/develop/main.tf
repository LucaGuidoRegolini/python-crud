module "dev" {
  source              = "../../infra"
  project-name        = var.TF_VAR_PROJECT_NAME
  region              = var.TF_VAR_AWS_REGION
  jwt_secret          = var.TF_VAR_JWT_SECRET
  database_url        = var.TF_VAR_DATABASE_URL
  aws_access_key      = var.TF_VAR_AWS_ACCESS_KEY
  aws_secret_key      = var.TF_VAR_AWS_SECRET_KEY
  project-environment = "develop"
  aplication_port     = 5000
  instance_ami_aws    = "ami-0fc5d935ebf8bc3bc"
  instance_type_aws   = "t2.micro"
  ssh_key_public      = var.TF_VAR_SSH_KEY_PUBLIC
}


resource "null_resource" "ansible_provision" {
  provisioner "local-exec" {
    command = <<EOT
    sudo ansible-playbook -i '${module.dev.IP},' playbook.yml \
      --private-key ./keys/project-key \
      -e "AWS_ACCESS_KEY=${var.TF_VAR_AWS_ACCESS_KEY}" \
      -e "AWS_SECRET_KEY=${var.TF_VAR_AWS_SECRET_KEY}" \
      -e "AWS_REGION=${var.TF_VAR_AWS_REGION}" \
      -e "AWS_USER_ID=${var.TF_VAR_AWS_USER_ID}" \
      -e "ECR_URL=${module.dev.ecr_repository_url}" \
      -e "PROJECT_PORT=5000" \
      -u ubuntu \
      -vvv
    EOT
  }

  # Espera que a instância esteja disponível antes de rodar o Ansible
  depends_on = [module.dev]
}
