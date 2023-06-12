resource "google_sql_database_instance" "my_sql_instance" {
  name             = var.cloud_sql_instance_name
  database_version = var.cloud_sql_database_version
  project          = var.project_id
  region           = var.region

  settings {
    tier      = var.cloud_sql_machine_type # Custom machine type with 2 vCPUs and 4GB of memory
    disk_type = "PD_SSD"
    ip_configuration {
      ipv4_enabled = true
    }
  }
}

resource "google_sql_user" "users" {
  name     = "admin"
  instance = google_sql_database_instance.my_sql_instance.name
  password = "admin"
}

resource "google_sql_database" "my_database" {
  name     = var.cloud_sql_dataset
  instance = google_sql_database_instance.my_sql_instance.name
}
