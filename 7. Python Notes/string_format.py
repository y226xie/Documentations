# Python String Formatiing

x = 12
print("some txt {} in the bracket".format(x))



quantity = 3 
iteno = 567
price = 49
myorder = "I want {} picese of item number {} for {:.2f} dollars"
print(myorder.format(quantity, itemno, price))

# index Numbers

quantity = 3 
iteno = 567
price = 49
myorder = "I want {0} picese of item number {1} for {2:.2f} dollars"
print(myorder.format(quantity, itemno, price))

# Named indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))