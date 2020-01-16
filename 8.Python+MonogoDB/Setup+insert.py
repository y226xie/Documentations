# Mongo DB
# Key-value pairs

# Database => Database
# Table => Collections
# Row => Documents
# Column => Field
# Primary key => Primary key (default key_id provided by monogodb itself)
# Mongodb stores data in documents.
# documents are just key - value pairs, but can include arrays and subdocuments. The data itself can be different data types like geospatial, decimal. and ISODate to name a few. Internally, MongoDB storesa a binary representation of JSON known as BSON, which allows MongoDB tp provide data types like decimal that are not defined in the JSON specification


# Commands for start mongodb in the mac
# To run mongodb as a macOS service: brew services start mongodb-community
# To stop mongodb as macOS service: brew services stop mongodb-community
# To verify that MongoDB is running: ps aux | grep -v grep | grep mongod
# Connect and us MongoDB: mongo
# install package by using pip: pip3 install package name

from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://wendy:0000@cluster0-crm83.mongodb.net/test?retryWrites=true&w=majority")
db = client['TestEnv']
# dblist = client.list_database_names()
# if "TestEnv" in dblist :
#     print("yes")

# In mongodb, a database is not created until it gets content!

col = db["health_info"]
# collist = db.list_collection_names()
# if "healthy_info" in collist: 
#     print("the collection exsits")

# user_info1 = {"name" : "John", "Height": 170}
# col.insert_one(user_info1) # insert_ont() method returns a InsertOneResult object, which has a property, `inserted_id`, that holds the id of the inserted document
# if we do not specify an _id field, then MongoDB will add one for you and assign a unqieu id for each document

users = [
    { "_id": 1, "name": "John", "address": "Highway 37"},
    { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
    { "_id": 3, "name": "Amy", "address": "Apple st 652"},
    { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
    { "_id": 5, "name": "Michael", "address": "Valley 345"},
    { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
    { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
    { "_id": 8, "name": "Richard", "address": "Sky st 331"},
    { "_id": 9, "name": "Susan", "address": "One way 98"},
    { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
    { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
    { "_id": 12, "name": "William", "address": "Central st 954"},
    { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
    { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]


ids = col.insert_many(users) #insert_many() method returns a insertManyResult object, which has a property inserted_ids, that holds the ids of the inserted documents
print(ids.inserted_ids) #holds the ids of the inserted documents

# If we do not want MongoDB to assign unique ids for the document, we can specify the _id field when we insert the document(s)
# Remember that the values has to be unique. Two documents cannot have the same_id





