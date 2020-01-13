# String literals in python are surrounded by either single quotation marks, or double quotation marks

# 'hello' is the same as "hello"
# Multiline Strings, we can assign a multiline string to a variable by using three quotes

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)

# Strings are Arrays
# Python does not have a character data type, a single character is simply a string with a lenghth of 1. square brakets can be used to access element of the string

c = "hello, World"
print(c[1])

# Slicing, get the characters from position 2 to position 5(not included): 
d = "Hello, World!" 
print(b[2:5])

# Negative Indexing, use negative indexes to start the slice from the end of the string: 

e = "Hello, World!" #orl
print(e[-5:-2]) 

# String length, to get length of a string, use len() function
f = "Hello, World!"
print(len(f))

# strip(), the strip method removes any whitespace from the beginning or the end
g = " Hello, World! "
print(g.strip()) # returns "Hello, World!"

# lower(), the lower method returns the string in lower case
l = " Hello, World! "
print(l.lower()) # hello, world!

# upper(), the upper method returns the string in upper case
m = " Hello, World! "
print(m.upper()) # HELLO, WORLD!

# replace(), the replace method replaces a string with another string
n = "Hello, World!"
print(n.replace("H", "J")) # Jello, World!

# split() method splits the string into substrings if it finds instances of the seperator:
o = "Hello, World!"
print(o.split(",")) # returns ["Hello", " World!"]

# Check String, to check if a certain phrase or character is present in a string, we can use the kyewords `in` or `not in`
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)
# true

# format()
# The format() method takes the paased arguments, formats them, and places them in the string where the placeholders `{}` are:

# Example 1
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# Example 2
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# Example 3
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape charater '\'
txt = "We are the so-called \"Vikings\" from the north"