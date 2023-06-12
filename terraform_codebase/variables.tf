variable "project_id" {
  description = "Google Project ID."
  type        = string
  default     = "workshop-project-0606"
}

variable "roles" {
  description = "Google Roles to assign to users"
  type        = list(string)
  default     = ["roles/storage.objectViewer"]
}

variable "region" {
  description = "GCP Region to deploy resources"
  type        = string
  default     = "us-central1"
}

variable "zone" {
  description = "GCP Zone to deploy resources"
  type        = string
  default     = "us-central1-c"
}

variable "bucket_name" {
  description = "A GCS bucket name"
  type        = string
  default     = "test-bucket"
}

variable "storage_class" {
  description = "Google Cloud region"
  type        = string
  default     = "STANDARD"
}

variable "location" {
  description = "Google Cloud location"
  type        = string
  default     = "US"
}


# variable "user_email_address" {
#   description = "Email id of Users"
#   type        = list(string)
#   default     = ["gurbanipradeep@gmail.com", "avenash97@gmail.com"]
# }

variable "user_details" {
  description = "Detail of Users"
  type        = list(map(any))
  default = [
    { "user_first_name" : "Pradeep", "user_last_name" : "Gurbani", "user_email_id" : "gurbanipradeep@gmail.com" },
    { "user_first_name" : "Avenash", "user_last_name" : "Ramesh", "user_email_id" : "avenash97@gmail.com" },
  ]
}

variable "cloud_sql_instance_name" {
  description = "Cloud SQL Instance"
  default     = "workshop-instance"
}

variable "cloud_sql_database_version" {
  description = "Cloud SQL Database version"
  default     = "MYSQL_8_0"
}

variable "cloud_sql_machine_type" {
  description = "Cloud SQL Machine Type"
}

variable "cloud_sql_dataset" {
  description = "Cloud SQL dataset"
  default     = "practice-dataset"
}