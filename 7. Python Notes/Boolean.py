# Boolean
# Basically, True or False

print(10 > 9)
print (10 == 9)
print (10 < 9)

# A basic example

a = 200
b = 33
if b > a :
    print("b is greater than a")
else :
    print("b is not greater than a")


# Evalute values and variables
# the bool() function allows you to evaluate any value, and give you `True` or `False` in return

print(bool("Hello")) #retun true
print(bool(15)) #return true

# Almost any value is evaluate to `true` if it has some sort of content
# Any string is True, except empty strings
# Any number is True, except 0
# Any list, tuple, set and dictionary are True, except empty ones

bool("abc")
bool(123)
bool(['a','b','c'])

# Values evalute to false: (), [], {}, "", 0, None, False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# object evalutes to False
# If we have an objects that are made from a class with a __len__ function that returns 0 or False

class myclass():
    def __len__(self) : # self represents the instance of the class. By using the `self` keyword we can access the attributes with the given arguments
        return 0

myobj = myclass()
print(bool(myobj))

# Functions can return a Boolean

# python also has many built-in functions that returns a boolean value, like the `isinstance()` function, which can be used to determine if an object is of a certain data type:

x = 200
print(isinstance(x, int)) # return true


