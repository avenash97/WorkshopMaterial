import csv
import os
import json
import logging

from google.cloud import pubsub_v1


def publish_to_topic (project_id, csv_file_path, topic_name):

    # Create a Pub/Sub client
    client = pubsub_v1.PublisherClient()

    # Create topic_path
    topic_path = client.topic_path(project_id, topic_name)
    
    # Read the CSV file
    with open(csv_file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)

    for row in reader:
        row.update({"First_Name": row.pop("First Name"), "Last_Name": row.pop("Last Name"), "Years_Of_Experience": row.pop("Years Of Experience"), "Job": row.pop("Job Title")})
        row["Title"] = row["Job"]
        row["Salary"] = int(row["Salary"])
        row["Years_Of_Experience"] = int(row["Years_Of_Experience"])
        message = json.dumps(row)

        # Publish the message
        future = client.publish(topic_path, message.encode("utf-8"))
        logging.info(f"Published message ID: {future.result()}")


def main():
    # Get config information
    with open("config.json") as f:
        config = json.load(f)
    
    # Get project-id
    project_id = config["gcp_project_id"]

    # Get topic name
    topic_name = config["pub_sub_topic_name"]

    # Get csv file path
    file_path = config["data_file_name"]
    csv_file_path = os.path.join(os.getcwd(), file_path)

    publish_to_topic(project_id=project_id, csv_file_path=csv_file_path, topic_name=topic_name)


if __name__ == "__main__":
    main()