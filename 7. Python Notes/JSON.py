# JSON in python

# Python has a built-in package called json, which can be used to work with JSON data

# import the json module

import json

# Pase JSON - Convert from JSON to Python
# If we have a JSON string, we can parse it by using the json.loads() method

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# Convert from python to JSON
# conver the Python object, convert it into a JSON string by using the json.dumps() method

import json

x = {
    "name": "John",
    "age" : 30,
    "city" : "New York"
}


y = json.dumps(x)
print(y)

# The following data structure can be convert into JSON strings: 

# dict => Object, list => Array, tuple => Array, string => string, int => Number, float => Number, True => true, False => false, None => Null


# Format the result
# the example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks. The `json.dumps()` method has parameters to make it easier to read the result


json.dumps(x, indent=4)

# We can define the separators parameter to change the default separator

json.dumps(x, indent = 4, separators = (". ", " = "))


# We can order the result by using the sort_keys property

json.dumps(x, indent=4, sort_keys=True) # sort it alphabetically
