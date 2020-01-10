# We can get the data type of any object by using the type() function
x = 5
print(type(x))

# String
a = 'Hello'

# int, or integer, is a whole number, positive or negative, without decimals, of unlimited length
b = 20

# float, or floating point number is a number, positive or negative, containing one or more decimals
# float can also be scientific numbers with an "e" to indicate the power of 10
c = 20.5
c = 12E4
c = 87.7e100

# complex, complex numbers are written with a "j" as the imaginary part
d = 1j

# list(array??)
e = ["apple", "Banana", "cherry"]

# tuple
f = ("apple", "banana", "cherry")

# range
g = range(6)

# dict
h = {"name": "John", "age": 36}

# set
i = {"apple", "banana", "cherry"}

# frozenset
l = frozenset({"apple", "banana", "cherry"})

# boolean
m = True

# bytes
n = b"Hello"

# bytearray
o = bytearray(5) # bytesarray(b'\x00\x00\x00\x00\x00')

# memoryview
p = memoryview(bytee(5)) # memory at 0x013D8FA0

# type conversion
q =  1
q = float(q)
q = complex(q)

# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called `random` that can be used to make random numbers

import random
print(random.randrange(1, 10))

