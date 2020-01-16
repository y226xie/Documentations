import pymongo

client = pymongo.MongoClient("mongodb+srv://wendy:0000@cluster0-crm83.mongodb.net/test?retryWrites=true&w=majority")
db = client['TestEnv']
col = db['health_info']

# data = col.find_one() # returns the first occurrence in the selection

# The find() method returns all occurrences in the selection, the first parameter of the find() us a query object. when the first parameter is empty, it selects all documents in the collection
# The second paramter of the find() method is an object describing which fields to include in the result. This parameter is optional, and if omitted, all fields will be included in the result

# for data in col.find() :
#     print(data)

# The following example basically exclude the name and _id property from searching result. However, we are not allowed to specify both 0 and 1 values in the same object (except if one of the firelds is the _id field). If we specify a field with the value 0, all other fields get the value 1 and vice versa
for val in col.find({}, {"name" : 0 , '_id': 0}) :
    print(val)



