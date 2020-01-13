# Python Lists
# Python collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changebale. Allows duplicate members
# Tuple is a collection which is ordered and unchangeable. Allow duplice members
# set is a collection which is unordered and unindexed. No duplicate members
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members

listA = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(listA)

# Access items
# You access the list items by referring to the index number
print(listA[1])

# Negative Indexing
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item
print(listA[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range. when specifying a range, the return value will be a new list with the specified items

# return the 3th, 4th, 5th item. The search will start at index2(included) and end at index 5(not included)
print(listA[2:5])

# By leaving out the start value, the range will start at the first item
print(listA[:4]) 

# By leaving out the last value, the range will end at the last item
print(listA[2:])

# Change Item Value
listA[1] = 'f'
print(listA)

# Looping through a list 
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# check if item exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# list length
thislist = ["apple", "banada", "cherry"]
print(len(thislist))

# append() - to add item to the end of the list 
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# insert() - to add an item at the specified index, use the insert() method
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# remove() - remove a specific item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# pop() - removes the specified index, (or the last item if index is not specified): 
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# del() - removes the specific index or the list completely
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist  
print (thislist) # return error, since thislist is already been deleted 

# clear() - clear method empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # retuns []

# Copy a list 
# if we simply copy a list by list2 = list1, then list2 will only be a reference to list1 and any change happens in list1 will also auto-update in list2

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# or we can use the built-in method list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join two lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# another way doing it is through append method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


# extend() method - you can use the extend() method, which purpose is to add elements from one list to another list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2) 
print(list1)


# list() constructor 
# It is also possible to use the list() constructor to make a new list
# using the list() contructor to make a list

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

