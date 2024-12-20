```
import pymongo

class MongoDBHandler:
    def __init__(self, uri='mongodb://localhost:27017/', db_name='sample_db', collection_name='sample_collection'):
        try:
            self.client = pymongo.MongoClient(uri)
            self.db = self.client[db_name]
            self.collection = self.db[collection_name]
            print(f"Connected to MongoDB at {uri}")
        except pymongo.errors.ConnectionError as e:
            print(f"Error connecting to MongoDB: {e}")
            exit(1)

    def create_document(self, document):
        try:
            if not isinstance(document, dict):
                raise ValueError("Document should be a dictionary")
            result = self.collection.insert_one(document)
            print(f"Document inserted with ID: {result.inserted_id}")
        except Exception as e:
            print(f"Error during create operation: {e}")

    def read_documents(self, query=None):
        try:
            query = query or {}
            documents = self.collection.find(query)
            document_list = list(documents)  # Convert cursor to a list for count checking

            if len(document_list) == 0:
                print("No documents found matching the query")
                return

            print("Documents in the collection:")
            for doc in document_list:
                print(doc)  # Simple print for the document

        except Exception as e:
            print(f"Error during read operation: {e}")

    def read_one_document(self, query):
        try:
            document = self.collection.find_one(query)
            if document:
                print("Single document retrieved:")
                print(document)  # Simple print for the document
            else:
                print("No document found matching the query")
        except Exception as e:
            print(f"Error during read operation: {e}")

    def update_document(self, query, update_data):
        try:
            if not isinstance(update_data, dict):
                raise ValueError("Update data should be a dictionary")

            result = self.collection.update_one(query, {'$set': update_data})

            if result.matched_count > 0:
                print(f"Matched {result.matched_count} document(s) and modified {result.modified_count} document(s)")
            else:
                print("No documents found to update")

        except Exception as e:
            print(f"Error during update operation: {e}")

    def delete_document(self, query):
        try:
            result = self.collection.delete_one(query)
            if result.deleted_count > 0:
                print(f"Deleted {result.deleted_count} document(s)")
            else:
                print("No document found to delete")
        except Exception as e:
            print(f"Error during delete operation: {e}")


# Main program to test the MongoDBHandler
if __name__ == "__main__":
    mongo_handler = MongoDBHandler()

    # Test CRUD operations
    document = {
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com",
        "address": "123 Main St"
    }

    # Create a document
    mongo_handler.create_document(document)

    # Read all documents
    mongo_handler.read_documents()

    # Read a specific document
    mongo_handler.read_one_document({"name": "John Doe"})

    # Update a document
    mongo_handler.update_document({"name": "John Doe"}, {"age": 31})

    # Read documents after update
    mongo_handler.read_documents()

    # Delete a document
    mongo_handler.delete_document({"name": "John Doe"})

    # Read documents after deletion
    mongo_handler.read_documents()

    ```
