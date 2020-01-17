#Limit the Result

# To limit the result in MongoDB, we use the limit() method
# The limit() method takes one parameter, a number defining how many documents to return

import pymongo

client = pymongo.MongoClient('mongodb+srv://wendy:0000@cluster0-crm83.mongodb.net/test?retryWrites=true&w=majority')

db = client['TestEnv']
col = db['health_info']

results = col.find().limit(5)

for result in results :
    print(result)