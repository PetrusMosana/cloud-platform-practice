terraform {
  required_version = ">= 1.5.0"
}

locals {
  environments = {
    dev = {
      instance_type = "t3.micro"
      cidr_block    = "10.0.0.0/16"
    }
    test = {
      instance_type = "t3.small"
      cidr_block    = "10.1.0.0/16"
    }
    prod = {
      instance_type = "t3.medium"
      cidr_block    = "10.2.0.0/16"
    }
  }
}

resource "terraform_data" "environment" {
  for_each = local.environments

  input = {
    project       = var.project_name
    environment   = each.key
    instance_type = each.value.instance_type
    cidr_block    = each.value.cidr_block
  }
}

output "environment_summary" {
  value = {
    for env, config in local.environments : env => {
      instance_type = config.instance_type
      cidr_block    = config.cidr_block
    }
  }
}