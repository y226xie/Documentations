# Python Iterators

# An iterator is an object that contains a countable number of values

# An iterator is an object that can be iterated upon, meaning that we can traverse through all the values

# Python has the iterator protocol, which consist of the methods __iter__() and __next__()

# Lists, tuples, dictionaries, and set are all iterable objects. They are iterable containers which we can get an iterator from

tup = ("apple", "banana", "cherry")
it = iter(tup)

print(next(it))
print(next(it))
print(next(it))


# Strings are also iterable objects, and can return an iterator

string = "banana"
str_it = iter(string)


print(next(str_it))
print(next(str_it))
print(next(str_it))

# we can use loop to loop though an iterator
tuples = ("apple", "banana", " cherry")
for x in the tuples:
    print(x)


# Iterate the characters of a string
mystr = "banana"
for letter in mystr:
    print(letter)

# The for loop actually creates an iterator object and executes the next() method for each loop!

# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

class numbers() :
    def __iter__(self):
        self.x = 1
        return self

    def __next__(self):
        a = self.x
        self.x = self.x + 1
        retrun a

# The __iter__() should return the iterator object itself
# The __next__() method should return the next item in the sequence

# StopIteration - to prevent the iteration to go on forever, we can use stopIteration statement

# in the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:

# stop after 20 iterations

class Numbers() :
    def __iter__ (self) :
        self.x = 1 
        return self
    
    def __next__ (self):
        if self.x < 20 :
            a = self.x
            self.x = self.x + 1
            return a 
        else :
            raise StopIteration
    