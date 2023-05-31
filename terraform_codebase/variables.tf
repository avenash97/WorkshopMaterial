variable "project_id" {
  description = "Google Project ID."
  type        = string
}

variable "zone" {
  description = "GCP Zone to deploy resources"
  type        = string
}


# variable "user_email_address" {
#   description = "Email id of Users"
#   type        = list(string)
#   default     = ["gurbanipradeep@gmail.com", "avenash97@gmail.com"]
# }

variable "user_details" {
  description = "Detail of Users"
  type = list(map(any))
  default = [
    { "user_first_name" : "Pradeep", "user_last_name" : "Gurbani", "user_email_id" : "gurbanipradeep@gmail.com" },
    { "user_first_name" : "Avenash", "user_last_name" : "Ramesh", "user_email_id" : "avenash97@gmail.com" },
  ]
}
