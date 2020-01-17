# # Delete Document

# # To delete one document, we use the delete_one() method
# # The first parameter of the delete_one() method is a query object defining which document to delete
# # But if the query finds more than one document, only the first occurrence is deleted

# import pymongo

# client = pymongo.MongoClient("mongodb+srv://wendy:0000@cluster0-crm83.mongodb.net/test?retryWrites=true&w=majority")

# db = client['TestEnv']
# col = db['health_info']

# query = {"address": "Mountain 21"}

# col.delete_one(query)

# for result in col.find():
#     print(result)



# Delete Many Documents
# to delete more than one document, use the delete_many() method
# The following example delete all documents were the address starts with the letter S

import pymongo

client = pymongo.MongoClient('mongodb+srv://wendy:0000@cluster0-crm83.mongodb.net/test?retryWrites=true&w=majority')
db = client['TestEnv']
col = db['health_info']


query = { "address": {"$regex" : "^S"}}

num = col.delete_many(query)
print(num.deleted_count, " documents deleted")

# Delete all documents in a collection
# To delete all documents in a collection, pass an empty query object to the delete_many() method

import pymongo

client = pymongo.MongoClient('mongodb+srv://wendy:0000@cluster0-crm83.mongodb.net/test?retryWrites=true&w=majority')
db = client['TestEnv']
col = db['health_info']

x = col.delete_many({})
print(x.deleted_count, "documents deleted")