import functions_framework
import json
import logging

from google.cloud import bigquery
from google.cloud import storage
from bq_schema import bigquery_table_schema


def upload_data(table_id):
  """Uploads data to BigQuery.

  Args:
    rows: The rows to upload.
    table_id: The ID of the table to upload to.

  """

  client = bigquery.Client()
  table = client.table(table_id)

  job_config = bigquery.LoadJobConfig()
  # job_config.schema = table.schema
  job_config.schema = bigquery_table_schema
  job_config.source_format = bigquery.SourceFormat.CSV
  job_config.skip_leading_rows = 1
  job_config.write_disposition = bigquery.WriteDisposition().WRITE_TRUNCATE

  load_job = client.load_table_from_uri(
      "gs://{}/{}".format(bucket_name, object_name),
      table_id,
      job_config=job_config)

  logging.info(load_job.result())



# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def hello_gcs(cloud_event):
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket = data["bucket"]
    name = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket}")
    print(f"File: {name}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {timeCreated}")
    print(f"Updated: {updated}")
    
    # # Read the file from Cloud Storage.
    # data = read_file(bucket_name, object_name)
    # # Process the data.
    # rows = process_data(data)

    with open("config.json") as f:
      config = json.load(f)
    
    table_id = config["bigquery_table_id"]
    
    # Upload the data to BigQuery.
    upload_data(table_id)