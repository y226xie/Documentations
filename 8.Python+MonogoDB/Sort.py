# Python MongoDB Sort
# Use the sort() method to sort the result in ascending or descending order
# The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is default direction)


import pymongo

client = pymongo.MongoClient("mongodb+srv://wendy:0000@cluster0-crm83.mongodb.net/test?retryWrites=true&w=majority")

db = client['TestEnv']
col = db['health_info']

results = col.find().sort("name")

for result in results:
    print (result)




# Sort Descending
# sort("name", 1) #ascending
# sort("name", -1) #descending

import pymongo

client = pymongo.MongoClient("mongodb+srv://wendy:0000@cluster0-crm83.mongodb.net/test?retryWrites=true&w=majority")
db = client['TestEnv']
col = db['health_info']

results = col.find().sort("name", -1)

for result in results:
    print(result)