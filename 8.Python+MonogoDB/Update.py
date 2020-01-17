# Update Collection
# We can update document by using the update_one() method
# The first parameter of the update_one() method is a query object defining which document to update
# If the query finds more than one document, only the first occurrence is updated
# The first parameter of the update_one() method is a query object defining which document to update
# The second parameter is an object defining the new values of the document


# import pymongo

# client = pymongo.MongoClient('mongodb+srv://wendy:0000@cluster0-crm83.mongodb.net/test?retryWrites=true&w=majority')

# db = client['TestEnv']
# col = db['health_info']


# old = {"address": "Valley 345"}
# new = {"$set": { "address": "Canyon 123"}}

# col.update_one(old, new)

# for val in col.find():
#     print(val)


# Update Many
# To update all documetns that meets the criteria of the query, use the update_many () method
import pymongo

client = pymongo.MongoClient('mongodb+srv://wendy:0000@cluster0-crm83.mongodb.net/test?retryWrites=true&w=majority')

db = client['TestEnv']
col = db['health_info']

old = { "address" : { "$regex" : "^S"}}
new = {"$set": {"address": "Fake street 123"}}

col.update_many(old, new)
for val in col.find() :
    print(val)
