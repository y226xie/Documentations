# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class

# Parent class is the class being inherited from, also called base class

# Child class is the class that inheirts from another class, also called derived class

# Create a parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()


class Student(Person) :
    def method(self):
        self.firstname = self.lastname
        print(self.firstname)


y = Student("Mike", "Olsen")
y.method()

# if we do not want to add any other properties or methods to the class
class HighSchoolStudents(Person):
    pass

# Add the __init__() Function 
# We have created a child class that inherits the properties and methods frim its parent

# if we add __init__() function to the child class, the child class will no longer inherit the parent's __init__() function

# The child's __init__() function overrides the inheritance of the parent's __init__() function

class Student(Person) :
    def __init__(self, fname, lname) :
        self.fname = fname
        self.lname = lname


# If we want to keep inheritance of the parent's __init__() function, we can add a call to the parent's __init__() function:

class Student(Person) :
    def __init__(self, fname, lname) :
        Person.__init__(self, fname, lname)


# or we can use Super() function to make the child class inherit all the methods and properties from its parent:

class Student(Person):
    def __init__(self, fname, lname) :
        super().__init__ (fname, lname)


# Add Properties

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
#   self.graductionyear = 2019
x = Student("Mike", "Olsen", 2019)

# Add Methods 
# If we add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)