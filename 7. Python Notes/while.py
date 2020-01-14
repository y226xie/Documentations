# Python while Loops
# with the while loop we can execute a set of statements as long as a condition is true

# A basic example 
i = 1
while i < 6 :
    print(i)
    i += 1

# the break statement
# with the break statment we can stop the loop even if the while condition is true

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# The continues statement
i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
print(i)


# The the else statement we can run a block of code once when the condition no longer is true: 
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")