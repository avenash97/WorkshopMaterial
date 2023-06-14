module "iam" {
  source             = "./modules/iam"
  for_each           = { for user_email_id in var.user_details : user_email_id.user_email_id => user_email_id }
  user_email_address = lower(each.value.user_email_id)
  project_id         = var.project_id
  roles              = var.roles
}

# module "compute_engine" {
#   source        = "./modules/compute_engine"
#   for_each      = { for user_details in var.user_details : user_details.user_email_id => user_details }
#   instance_name = format("%v-%v-%v", lower(each.value.user_first_name), lower(each.value.user_last_name), each.value.user_id)
#   zone          = var.zone
#   project_id    = var.project_id
# }

# # Create GCS bucket
# module "cloud_storage" {
#   source        = "./modules/cloud_storage"
#   project_id    = var.project_id
#   storage_class = var.storage_class
#   bucket_name   = format("%v-%v", each.value.project_id, var.bucket_name)
#   location      = var.location
# }


# Create Cloud SQL Instance and Dataset
module "cloud_sql" {
  source                     = "./modules/cloud_sql"
  project_id                 = var.project_id
  region                     = var.region
  cloud_sql_instance_name    = var.cloud_sql_instance_name
  cloud_sql_database_version = var.cloud_sql_database_version
  cloud_sql_machine_type     = var.cloud_sql_machine_type
  cloud_sql_dataset          = var.cloud_sql_dataset
}