# Python For Loops
# For loop in python is more like an iterator method compared to other oop language

# Basic example
arr = [1, 2, 3, 4, 5, 6, 7]
for x in arr:
    print(x)

# Looping though string
for x in "banana" :
    print(x)

# Range() function
# To loop through a set of code a specified number of times, we can use the range() fucntion. The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 , and ends at a specified number

for x in range(6) :
    print(x)
# 0, 1, 2, 3, 4, 5 


for x in range(2,6) :
    print (x)
# 2, 3, 4 ,5


for x in range (2, 30, 3) : # the range() function defaults to increment the sequence by 1, the third param allows to increment the sequence with 3
    print(x)


# Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# For loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error

for x in [0, 1, 2]
    pass

