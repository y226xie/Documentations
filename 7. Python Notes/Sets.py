# Set
# A set is a collection which is unordered an unindexed.

# Since is unindexed, we cannot access items in a set by referring to an index, since sets are unordered the items has no index

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)


# add() - to add one item to a set use the add() method
# update() - to add more than one item to a set use the update() method

thisset = {"apple", "banana", "cherry"}
thisset.add("orange") 


thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])

# Length of the set
print(len(thisset))


# Remove item - but if the item does not exist, this will return an error
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")

# Discard () - Remove "banana" by using the discard() method. If the item to remove does not exist, discard() will NOT raise an error
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# You can also use the pop(), method to remove an item, but this method will remove the last item. Since the set is unordered, so you will not know what item that gets removed

thisset = { "apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# clear() - the clear() method empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# the del keyword will detele the set completely
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

# Join two sets - union() - update()
# there are several ways to join two or more sets in Python
# union() - returns a new set with all items from both sets
set1 = { "a", "b", "c" }
set2 = { 1, 2, 3}
set3 = set1.union(set2)
print(set3)


# update() - insert new items from set2 into set1
set1 = { "a", "b", "c"}
set2 = { 1 , 2, 3}
set1.update(set2)
print(set1)

# set()
# The set() constructor - it is also possible to use the set() constructor to make a set

thisset = set(("apple", "banana", "cherry"))
print(thisset)





