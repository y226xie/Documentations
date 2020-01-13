# Dictionary
# A dictionary is a collection which is unordered, changeable an indexed. In python dictionaries are written with curly brackets, and they have keys and values

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Accessing items
x = thisdict["model"] # or we can do x = thisdict.get("model")

# Change Values 
thisdict["year"] = 2020

# Looping though a dictionary
for x in thisdict: # print all key names in the dictionary
    print(x)


for x in thisdict:
    print(thisdict[x]) # print all values in the dictionary, one by one

# values() - returns values of a dictionary
for x in thisdict.values()
    print(x)

# Loop though both keys and values, by using items() function
for x, y in thisdict.items():
    print(x,y)

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# Removing items
# pop() - removes the item with the specified key name
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# popitem() - remove the last inserted item
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# del - removes the item with the specified key name: 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# del keyword can also delete the dictionary completely
del thisdict

# clear() - empties the dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# copy() - make a copy of a dictionary with the copy() method
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Make a copy of a dictionary with the dict() method: 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# dict() constructor
thisdict = dict(brand="ford", model="mustang", year=1964)
print(thisdict)