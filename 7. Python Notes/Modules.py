# Module
# Module is similar to code library
# A file containning a set of functions you want to include in your application

# Create a Module
# To create a module, we just save the code we want in a file with extension .py

# A basic example

def greeting(name) :
    print ("Hello, " + name)

# save this code in a flie named mymodule.py

# we can use the module we just created by using `import` statement

import mymodule
mymodule.greeting("Wendy") # when useing a function from a module, use the syntax module_name.function_name

# Variables in Module
# The module can contain functions, as already described , but also variables of all types (arrays, dictionaries, objects etc) :

person1 = {
    "name" : "John",
    "age"  : 36,
    "country" : "Norway"
}

import mymodule

a = mymodule.person1["age"]
print(a) # 36


# Renaming a module

import mymodule as mx

a = mx.person1["age"]
print(a)


# Built-in Modules

import platform
x = platform.system()
print(x)


import platform
x = dir(platform)
print(x)


# Import from module
# We can choose to import only parts from a module, by using the `from` keyword

# The module named mymodule has one function and one dictionary

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# import only person1 from mymodule
from mymodule import person1

print (person1["age"])