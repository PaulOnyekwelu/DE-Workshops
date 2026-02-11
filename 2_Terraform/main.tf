terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.16.0"
    }
  }
}

provider "google" {
  credentials = "./keys/terra.json"
  project     = "terraform-project-485222" # this is the project ID
  region      = "EUROPE-WEST2"
}


resource "google_storage_bucket" "demo-bucket" {
  name          = "terraform-project_demo-bucket"
  location      = "EUROPE-WEST2"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}