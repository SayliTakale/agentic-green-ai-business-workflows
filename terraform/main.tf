# Dummy Terraform configuration
# Purpose: Demonstrate infrastructure automation awareness
# No real cloud resources are provisioned

terraform {
  required_version = ">= 1.0.0"
}

provider "local" {
}

resource "local_file" "green_ai_info" {
  filename = "terraform_demo.txt"
  content  = "Terraform placeholder for Green AI workflow automation"
}
