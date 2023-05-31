module "iam" {
  source     = "./modules/iam"
  for_each   = { for user_email_id in var.user_details : user_email_id.user_email_id => user_email_id }
  user_email_address = lower(each.value.user_email_id)
  project_id = var.project_id
}

module "iam" {
  source     = "./modules/compute_engine"
  for_each   = { for user_id in var.user_details : user_id.user_first_name => user_first_name }
  instance_name = format("%v-%v", lower(each.value.user_first_name), lower(each.value.user_last_name))
  zone = var.zone
  project_id = var.project_id
}