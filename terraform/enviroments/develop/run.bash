#!/bin/bash
mkdir -p ./keys

TFVARS_FILE="./variables.tfvars"

if [ ! -f "./keys/project-key" ]; then
    ssh-keygen -t rsa -b 4096 -C "project-key" -f "./keys/project-key" -N ""
        # Adiciona a linha se não existir
    SSH_KEY_PUBLIC=$(cat ./keys/project-key.pub)
    echo "TF_VAR_SSH_KEY_PUBLIC=\"$SSH_KEY_PUBLIC\"" >> "$TFVARS_FILE"
    chmod 644 ./keys/project-key
    chmod 644 ./keys/project-key.pub
else
    echo "A chave SSH já existe em ./keys/project-key"
fi

terraform init
terraform apply -var-file=variables.tfvars -auto-approve

ELASTIC_IP=$(terraform output -raw ELASTIC_IP)

echo "Elastic IP: $ELASTIC_IP"