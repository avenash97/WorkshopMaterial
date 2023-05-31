from google.cloud import bigquery

bigquery_table_schema = [
        bigquery.SchemaField("First Name", "STRING"),
        bigquery.SchemaField("Last Name", "STRING"),
        bigquery.SchemaField("Email", "STRING"),
        bigquery.SchemaField("Phone", "STRING"),
        bigquery.SchemaField("Gender", "STRING"),
        bigquery.SchemaField("Department", "STRING"),
        bigquery.SchemaField("Job", "STRING"),
        bigquery.SchemaField("Title", "STRING"),
        bigquery.SchemaField("Years Of Experience", "INTEGER"),
        bigquery.SchemaField("Salary", "INTEGER"),
        ]