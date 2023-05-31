import json
# import firebase_admin
# from firebase_admin import firestore

from google.cloud import firestore

# Initialize the Firestore client
# firebase_admin.initialize_app()

# Get the Firestore database
db = firestore.Client()

# Read the JSON file
with open("employees-updated.json") as f:
  data = json.load(f)

# Create a Firestore collection
collection = db.collection("test-collection")

# Iterate over the data and add it to the collection
for item in data["employees"]:
    print(item)
    print(type(item))
    collection.document("Employee-" + str(item["id"])).set(item)

# Print a success message
print("Data successfully uploaded to Firestore!")

###### TO DELETE ALL THE DOCUMENTS IN A COLLECTION #####

# # Get the collection reference
# collection_ref = db.collection("test-collection")

# # Delete all the documents in the collection
# docs = collection_ref.list_documents()

# for doc in docs:
#     print(f'{doc.id} => {doc.get().to_dict()}')
#     doc.delete()

# # Print a success message
# print("All documents in the 'test-collection' collection have been deleted!")

###### TO QUERY THE DOCUMENTS IN A COLLECTION WHERE SALARY IS MORE THAN A GIVEN NUMBER #####

# employees_ref = db.collection('test-collection')

# query = employees_ref.where('salary', '>=', 7000)

# results = query.get()
# print(results)

# # Print the results
# for result in results:
#     print(result.to_dict())

###### TO QUERY THE DOCUMENTS IN A COLLECTION WHERE PTOs FIELD EXISTS IN A DOCUMENT #####

# Get the collection reference
# collection_ref = db.collection("test-collection")

# # Query the collection
# query = collection_ref.where("PTOs", "==", None)

# # query = collection_ref.where

# # Get the results
# results = query.get()
# print(results)

# # Print the results
# for result in results:
#   print(result.to_dict())

# docs = db.collection('test-collection').stream()

# for doc in docs:
#     if "PTOs" in doc.to_dict():
#         print(f'{doc.id} => {doc.to_dict()}')
#     else:
#         pass
