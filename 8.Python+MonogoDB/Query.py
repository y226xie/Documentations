# Python MongoDB Query

# Filter the result
# when finding documents in a collection, we can filter the result by using a query object
# the first argument of the find() method is a query object, and is used to limit the search

# Example : Find document with the address "Park Lane 38"

import pymongo

client = pymongo.MongoClient("mongodb+srv://wendy:0000@cluster0-crm83.mongodb.net/test?retryWrites=true&w=majority")
db = client['TestEnv']
col = db['health_info']

query = {"address" : "Park Lane 38"}

items = col.find(query) # returns the info has that query info

for item in items :
    print(item)


# Advanced Query

# To make advanced queries we can use modifiers as values in the query obejct
# Find documents where the address starts with the letter "S" or higher
import pymongo

client = pymongo.MongoClient("mongodb+srv://wendy:0000@cluster0-crm83.mongodb.net/test?retryWrites=true&w=majority")
db = client['TestEnv']
col = db['health_info']

query = { "address" : { "$gt" : "S"}}

infos = col.find(query)

for item in infos:
    print(item)


# Filter with regular expressions

# regular expressions can be used to query strings!!!!
import pymongo

client = pymongo.MongoClient("mongodb+srv://wendy:0000@cluster0-crm83.mongodb.net/test?retryWrites=true&w=majority")
db = client["TestEnv"]
col = db["health_info"]

query = {"address": {"$regex": "^S"}} # only returns the items that begin with S for address info

results = col.find(query)
for result in results:
    print(result)



