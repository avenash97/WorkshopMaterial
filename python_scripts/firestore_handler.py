import json
import logging

from google.cloud import firestore

# Initialize FireStore Client
db = firestore.Client()


def add_data_to_collection(collection_name, data):
  """Uploads data to Firestore collection.

  Args:
    collection_name: The name of collection, where data is to be uploaded
    data: List of dictionaries to be uploaded

  """

  # Create a Firestore collection
  collection = db.collection(collection_name)

  # Iterate over the data and add it to the collection
  for item in data["employees"]:
    collection.document("Employee-" + str(item["id"])).set(item)

  # Print a success message
  logging.info("Data successfully uploaded to Firestore!")


###### TO DELETE ALL THE DOCUMENTS IN A COLLECTION #####
def delete_data_from_collection(collection_name):
  
  # Get the collection reference
  collection_ref = db.collection(collection_name)

  # Delete all the documents in the collection
  docs = collection_ref.list_documents()

  for doc in docs:
      logging.info(f'{doc.id} => {doc.get().to_dict()}')
      doc.delete()

  # Print a success message
  logging.info(f"All documents in the {collection_name} collection have been deleted!")


###### TO QUERY THE DOCUMENTS IN A COLLECTION WHERE SALARY IS MORE THAN A GIVEN NUMBER #####
def query_collection(collection_name):
  
  employees_ref = db.collection(collection_name)

  query = employees_ref.where('salary', '>=', 7000)

  results = query.get()
  print(results)

  # Print the results
  for result in results:
      print(result.to_dict())


###### TO QUERY THE DOCUMENTS IN A COLLECTION WHERE PTOs FIELD EXISTS IN A DOCUMENT #####
def custom_query_collection(collection_name):

  docs = db.collection(collection_name).stream()

  for doc in docs:
    if "PTOs" in doc.to_dict():
      print(f'{doc.id} => {doc.to_dict()}')
    else:
      pass


def main():
  
  # Get config information
  with open("config.json") as f:
    config = json.load(f)
    
  # Get firestore collection name
  collection_name = config["collection_name"]

  # Get the JSON data file path
  json_data_file_path = os.path.join(os.getcwd(), config["json_data_file_path"])

  # Read the JSON data
  with open(json_data_file_path) as f:
    data = json.load(f)

  add_data_to_collection(collection_name=collection_name, data=data)
  
  # delete_data_from_collection(collection_name=collection_name)
  # query_collection(collection_name=collection_name)
  # custom_query_collection(collection_name=collection_name)


if __name__ == "__main__":
    main()