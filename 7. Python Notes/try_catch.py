# try_catch statements in Python

# The try block lets you test a block of code for errors 
# The except block lets you handle the error
# The finally block lets you execute code, regardless of the result of the try- and expect blocks


# Basic structures
try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Somthing went wrong when writing to the file")
finally: 
    f.close()

# Raise an exception
# To throw an exception, use the `raise` keyword

x = -1
if x < 0 :
    raise Exception("sorry, something went wrong")


