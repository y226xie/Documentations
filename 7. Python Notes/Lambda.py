# Python Lambda
# A lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression

# syntax
# lambda arguments : expression

# A lambda function that adds 10 to the number passed in as an argument, and print the result

# Python way of supporting functional programming language

x = lambda a :  a + 10
print (x(5))

mult3 = filter(lambda x: x % 3 == 0, 1, 2, 3, 4, 5, 6])

def filterfunc(x) :
    return x % 3 == 0
multi3 = filter(filterfunc, [0, 1, 2, 3, 4, 5, 6])

# This is often used to create function wrappers, such as decorators
def transform(n) :
    return lambda x : x + n

f = transform(3)
f(4) # return 7




