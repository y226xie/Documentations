# Arrays
# Basic syntax 

cars = ["Ford", "Volvo", "BMW"]

# An array is a spefial variable which can hold more than one value at a time
# An array can hold many values under a single name, and you can access the values by referring to an index number

# Access the elements of an array
x = cars[0]

length = len(cars)

# Looping array elements 
for x in cars: 
    print(x)


# Adding items can use append()
cars.append("sth")

# Removing array elements 
cars.pop(1) # Delete the second element of the cars array
cars.remove("BMW")

