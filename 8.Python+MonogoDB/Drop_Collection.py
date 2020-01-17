# Delete Collection
# We cam delete a table, or collection as it is called in MongoDB, by using the drop() method

import pymongo

client = pymongo.MongoClient('mongodb+srv://wendy:0000@cluster0-crm83.mongodb.net/test?retryWrites=true&w=majority')

db = client['TestEnv']
col = db['health_info']

x = col.drop()
print(x)