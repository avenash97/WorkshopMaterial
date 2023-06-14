# Create Google Storage Bucket
resource "google_storage_bucket" "storage" {
  project                     = var.project_id
  name                        = var.bucket_name
  location                    = var.location
  storage_class               = var.storage_class
  force_destroy               = true
  uniform_bucket_level_access = true
  versioning {
    enabled = true
  }
}

# Create Data Folder in GCS bucket
resource "google_storage_bucket_object" "folder_data" {
  name    = "data/"
  content = "Empty folder for storing data"
  bucket  = google_storage_bucket.storage.name
}