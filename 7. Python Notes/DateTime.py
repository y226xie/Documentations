# Python Dates
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects

import datetime 

x = datetime.datetime.now()
print(x) #2020-01-15 11:23:48.474521


import datetime

x = datetime.datetime.now()

print(x.year) # 2020
print(x.strftime("%A")) #Wednesday

# Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime modul
import datetime
 
x = datetime.datetime(2020, 5, 17)
print(x)

# Strftime() method
# Formatting date objects into reable strings, the method is called strftime(), and takes one parameter `format`, to specify the format of the returned string: 

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B")) # month name, full version


