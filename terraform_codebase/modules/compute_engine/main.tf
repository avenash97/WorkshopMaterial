resource "google_compute_instance" "practice_instance" {
  name         = var.instance_name
  project      = var.project_id
  machine_type = "e2-micro"
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    # access_config {
    #   // Ephemeral IP address
    # }
  }

  #   metadata {
  #     startup_script = <<EOF
  #     apt update
  #     apt install -y gcloud
  #     EOF
  #   }

  tags = ["allow-all-gcloud-apis"]
}