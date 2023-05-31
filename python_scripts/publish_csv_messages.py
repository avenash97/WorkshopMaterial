import csv
import os
import json

from google.cloud import pubsub_v1

# Get the path to the CSV file
with open("config.json") as f:
    config = json.load(f)

data_file_name = config["data_file_name"]
csv_file_path = os.path.join(os.getcwd(), data_file_name)

# Create a Pub/Sub client
client = pubsub_v1.PublisherClient()

# Create a topic
topic_name = config["pub_sub_topic_name"]
topic = client.topic_path("sadaindia-tvm-poc-de", topic_name)


# Read the CSV file
with open(csv_file_path, "r") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        row.update({"First_Name": row.pop("First Name"), "Last_Name": row.pop("Last Name"), "Years_Of_Experience": row.pop("Years Of Experience"), "Job": row.pop("Job Title")})
        row["Title"] = row["Job"]
        row["Salary"] = int(row["Salary"])
        row["Years_Of_Experience"] = int(row["Years_Of_Experience"])
        message = json.dumps(row)
        print(message)

        # Publish the message
        future = client.publish(topic, message.encode("utf-8"))
        print(f"Published message ID: {future.result()}")