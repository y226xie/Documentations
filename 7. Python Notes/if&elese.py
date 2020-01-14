# If statements

# Basic example

a = 33
b = 200
if b > a :
    print("b is greater than a")

# Elif - else if

a = 33
b = 33
if b > a :
    print("some stuff")
elif a == b :
    print("nothing")


# Else

a = 200
b = 33
if b > a :
    print("a message")
elif a == b :
    print (" this is alos a message")
else :
    print("a is greater than b")

# The Pass statement
# if statements cannot ve emnpty, but if you for some reason have an if statment with no content put in the pass statement to avoid getting an error

a = 33
b = 200
if b > a :
    pass