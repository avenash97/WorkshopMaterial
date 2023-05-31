resource "google_project_iam_binding" "compute_engine" {
  role = "roles/compute.viewer"
  members = ["user:${user_email_address}"]
}

resource "google_project_iam_binding" "gcs" {
  role = "roles/storage.objectViewer"
  members = ["user:${user_email_address}"]
}

resource "google_project_iam_binding" "bigquery" {
  role = "roles/bigquery.dataViewer"
  members = ["user:${user_email_address}"]
}

resource "google_project_iam_binding" "bigquery_pubsub" {
  role = "roles/bigquery.jobUser"
  members = ["user:${user_email_address}"]
}

resource "google_project_iam_binding" "cloud_function" {
  role = "roles/cloudfunctions.dev"
  members = ["user:${user_email_address}"]
}

resource "google_project_iam_binding" "cloud_sql" {
  role = "roles/cloudsql.client"
  members = ["user:${user_email_address}"]
}

resource "google_project_iam_binding" "pubsub" {
  role = "roles/pubsub.editor"
  members = ["user:${user_email_address}"]
}

resource "google_project_iam_binding" "firestore" {
  role = "roles/firestore.documentViewer"
  members = ["user:${user_email_address}"]
}


# This code will assign the following permissions to the users in GCP environment:

# * Compute Engine permission to view the instance creation page and SSH into the instances and not spin up or delete the instances
# * GCS permission to read/write objects and not create or delete the bucket
# * BigQuery permission to allow creation of table in a given dataset and query it. Also to subscribe the Pub/Sub topic
# * Cloud Function permission to deploy only 1 function with lowest configuration
# * Cloud SQL permission to access the dataset and table in the provided Cloud SQL instance and don't allow to create a new instance
# * Pub/Sub permission to create topics and let BigQuery table subscribe to it
# * Firestore permission to read/write a collection and not create any new collection

# Please note that you will need to replace `${user_email_address}` with your actual email address in the code.