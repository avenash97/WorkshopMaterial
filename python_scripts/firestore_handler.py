import json
import os
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

def document_data_update(collection_name: str, document_id: str, firestore_value: dict) -> None:
    """Updates key value pair in a Document under a collection

    Args:
        collection_name: Firestore collection name
        document_id: Firestore document id
        firestore_value: Dictionary with value to be updated in Firestore
    """
    # Create a Firestore document ref under a collection
    doc_ref = db.collection(collection_name).document(document_id)

    # Updates the respective document id with the new values
    doc_ref.update(firestore_value)

    # logging the success message
    logging.info("Document successfully updated!")



def delete_data_from_collection(collection_name: str, document_id: str = None, all_documents: bool = False) -> None:
    """To delete particular document id or all documents from the collection

    Args:
        collection_name : Firestore collection name
        document_id : Firestore document id. Defaults to None.
        all_documents : Flag to delete all documents inside a collection. Defaults to False.
    """
    # Get the collection reference
    collection_ref = db.collection(collection_name)

    if all_documents:
        # Delete all the documents in the collection
        docs = collection_ref.list_documents()

        for doc in docs:
            logging.info(f'{doc.id} => {doc.get().to_dict()}')
            doc.delete()

        # logging the success message
        logging.info(f"All documents in the {collection_name} collection have been deleted!")  
    else:
        # Delete the respective document
        collection_ref.document(document_id).delete()

        # logging the success message
        logging.info(" Document id {} in the {} collection have been deleted!".format(document_id, collection_name))


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