# Python functions

# Creating a function - a function is defined using the def keyword

def my_function():
    print("a message")

my_function() # calling a function

# Arguments - arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, separate by a comma

def function(param) :
    print (param + "idk")

function("email")

# Parameters or Arguments
# A param is the variable listed inside the parentheses in the function definition
# A argument is the value that are sent to the function when it is called 

# Number of arguements
# By defualt, a function must be called with the correct number of arguments. If the function expects 2 arguments, you have to call the funtion with 2 arguements

def my_function(fname, lname): 
    print(fname+ " " + lname)

my_function("first", "last")

# arbitrary arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition. This way the function will receive a tuple of arguments, and can access the items accordingly

def my_function(*people) :
    print ("that person is" + people[2])

my_function("Person A" , "Person B", "Person C")

# Keyword Arguments
# We can send arguments with the key = value syntax, this way order of the arguments does not matter

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments **kwargs
# If we not sure how many keyword arguements that will be passed into our funtion, add two asterix ** before the parameter name in the function definition

# If we have a dictionary of arguments, and can access the items accordingly
# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**people) : 
    print("this person's last name is " + people["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Default parameter value
def my_function (country = "Canada") :
    print("I am from " + country)
my_function("China")


# Passing a list as an argument
# you can send any data types of argument to a function (string, number, list, dictionary)...

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# The pass statement
# Function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error 

def myfunction():
  pass



# Recursion

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)