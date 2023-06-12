project_id = "workshop-project-0606"
region     = "us-central1"
zone       = "us-central1-c"
user_details = [
  { "user_first_name" : "Pradeep", "user_last_name" : "Gurbani", "user_email_id" : "gurbanipradeep@gmail.com", "user_id" : "1" },
]
roles = ["roles/compute.viewer", "projects/workshop-project-0606/roles/custom_role", "roles/iap.tunnelResourceAccessor", "roles/storage.admin", "roles/bigquery.dataViewer", "roles/bigquery.admin", "roles/cloudfunctions.developer", "roles/cloudsql.editor", "roles/pubsub.editor", "roles/datastore.user"]
# roles = ["roles/compute.viewer"]

cloud_sql_instance_name    = "workshop-instance"
cloud_sql_database_version = "MYSQL_8_0"
cloud_sql_machine_type     = "db-custom-2-4096"

cloud_sql_dataset = "practice-dataset"