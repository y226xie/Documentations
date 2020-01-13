# Tuple
# A tuple is a collection which is ordered and unchangeable. In Python, tuples are written with round brackets

# create a tuple 
thistuple = ('apple', 'banana', 'cherry')
print(thistuple)

# access the tuple items 
thistuple = ('apple', 'banana', 'cherry')
print(thistuple[1])

# Change Tuple values
x = ('a','b', 'c')
y = list(x)
y[1] = 'k'
x = tuple(y)
print(x)

# Loop through the items
thisnewtuple = ('a', 'b','c')
for x in thisnewtuple:
    print(x)


# check if item exists
# check if "apple" is present in the tuple

thisoldtuple = ('a', 'b', 'c')
if 'a' in thisoldtuple :
    print('yes')


# Tuple Length 
# To determine how many items a tuple has, use the len() method

thistuple = ('a', 'b', 'c')
print((len(thistuple)))


# Create tuple with one item
# To create a tuple with only one item, you have add a comma after the item, unless python will not recognize the variable as a tuple

thistuple = ("apple",)
print(type(thistuple)) # return <class 'tuple'>

thistuple = ("apple")
print(type(thistuple)) #return <class 'str'>

# since tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely

# The del keyword can delete the tuple completely
thistuple = ('a', 'b', 'c')
del thistuple
print(thistuple) # this will rais an error because the tuple no longer exists

# Join Two Tuples
# To join two or more tuples you can use the `+` operator

tuple1 = ('a', 'b','c')
tuple2 = (1,2,3)

tuple3 = tuple1 + tuple2
print(tuple3)

# The Tuple() constructor 
# It is also possible to use the tuple() constructor to make a tuple

tuple4 = tuple(('apple', "banana"))
print(tuple4)


