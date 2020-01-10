# Python Casting
# Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types

# Casting in python is therefore done using constructor functions: 

"""
int() - constructs an integer number from an integer literal, a float literal(by rounding down to the previous whole number)

float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)

str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""


#int()
x = int(1)   # 1
y = int(2.8) # 2
z = int("3") # 3

#float()
a = float(1)  # 1.0
b = float(2.8) # 2.8
c = float ("3") # 3.0
d = float("4.2") # 4.2

#str()
e = str("s1") # 's1'
f = str(2)    # '2'
g = str(3.0)  # '3.0'