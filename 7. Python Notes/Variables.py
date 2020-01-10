# Some basics:
# Use this symbol for adding comments section
# There is no semicolon, curly braces in python. In Python3 everything is object

"""
Having multiple comments
"""

# Variables
# In python, variables are created when you first assign value to them
# variables don't need to be declared with any particular type and can even change type after they have been set
# Strings can be used either double quote or single quote
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# Variable names are case-sensitive
x = 5
y = "people"
y = 'people'
print(x)

z, n, m = "orange", "Banana", "Cherry"
print(z)
print(n)
print(m)

# Output variables
# We can use the `+` character to combine text
# for numbers, the `+` works as the mathematical operator
# but if we are trying to combine a string and a  number, python will give us an error
a = "not ok"
print("Python is " + a)

b = 3
c = 4
print(b+c)

# Global Variables
# variables create outside of a funtion are gloabl variables
# variables outside of a function
d = 'some stuff'

def myfunc():
    print (d)

myfunc()


# variables inside of a function

e = "good"

def efunc():
    e = "bad"
    print("Python is " + e)

efunc()

# we can create a global variable inside a function, we can use the `global` keyword
def mynewfunc():
    global p
    p = "fantastic"

mynewfunc()

# To Change a gobal variable inside a function, refer to the variable by using global keyword

var = "awesome"

def changeVar(): 
    global var 
    var = "good"

changeVar()
print("python is "+ var)



