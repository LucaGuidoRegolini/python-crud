variable "region" {
  default = "us-west-2"
}

variable "aws_access_key" {
  description = "value of the aws access aws key"
  type        = string
}

variable "aws_secret_key" {
  description = "value of the aws secret aws key"
  type        = string
}

variable "project-name" {
  description = "Name of the project"
  type        = string
}

variable "project-environment" {
  description = "Environment of the project"
  type        = string
}

variable "ssh_key_public" {
  description = "value of the ssh public key"
  type        = string
}

variable "instance_ami_aws" {
  type = string
}

variable "instance_type_aws" {
  type = string
}

variable "database_url" {
  type = string
}

variable "jwt_secret" {
  type = string
}

variable "aplication_port" {
  type = string
}
