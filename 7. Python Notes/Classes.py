# Python Classes/Objects

# Almost everything in python is an object, with its properties and methods

# A class is like an object constructor, or a "blueprint" for creating objects

# A basic example

class myClass:
    x = 5

p1 = myClass()
print(p1.x)

# The __init__() function, all classes have a function called __init__(), which is always executed when the class is being initiated

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created

# the __init__() function is called automatically every time the class is being used to create a new object


class Person:
    def __init__(self, name, age): 
        self.name = name
        self.age = age

p1 = Person("wendy", 20)

print(p1.name)
print(p1.age)


# Object Methods
class Person:
    def __init__(self, name, age): 
        self.name = name
        self.age = age
    def func(self):
        print("hello, my name is" + self.name)

p1 = Person("wendy", 20)
p1.fucn()


# The `self` parameter is a reference to the current instance of the class and is used to access variables that belong to the class

# It does not have to be named `self`, we can call it whatever, but it must be the first parameter of any function in the class

# Modify Object properties
p1.age = 40

# Delete the properties on objects by using the del keyword
del p1.age

# Delete objects
del p1

# Pass Statement
# Class definitions cannot be empty, but if for some reason we have a class definition with no content, put the pass statement to avoid getting an error

class Person:
    pass



