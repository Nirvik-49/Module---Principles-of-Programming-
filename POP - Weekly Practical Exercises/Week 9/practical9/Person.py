# Person class with private attributes and __str__
# Practical 9 - Exercise 2 - Task 2.1
# Nirvik K.C.

class Person:
    # Constructor with default values
    def __init__(self, firstName='Mr', lastName='X', address='Bristol'):
        self.__firstName = firstName   # private variable
        self.__lastName  = lastName    # private variable
        self.__address = address       # private variable

    # Setters
    def setFirstName(self, firstName):
        self.__firstName = firstName

    def setLastName(self, lastName):
        self.__lastName = lastName

    def setAddress(self, address):
        self.__address = address

    # Getters
    def getFirstName(self): 
        return self.__firstName 
 
    def getLastName(self): 
        return self.__lastName
    
    def getAddress(self):
        return self.__address
    
    # Use of __str__method
    def __str__(self): 
        return "Person's name is " + self.getFirstName() +" "+ self.getLastName() +"\nAddress is "+ self.getAddress()
    
# Test program

# Creating a Person object with default values 
print("Creating a Person object with default values") 
p =  Person()

# Printing the information using __str__ method 
print("Printing the information using __str__ method") 
print(p) 

# Setting name and address 
print("Now setting the names and address") 
p.setFirstName("Abdur") 
p.setLastName("Rakib")
p.setAddress("UWE Frenchay Campus 4QXX") 

# Printing the information using __str__ method 
print("Printing the information using __str__ method") 
print(p)

# Creating another object by passing values explicitly
print("Creating another Person object by passing the values explicitly") 
p1 = Person("Jun", "Hong", "UWE Frenchay Campus 3QXX")

# Printing the information using __str__ method 
print("Printing the information using __str__ method")
print(p1)

# Output:
# Creating a Person object with default values
# Printing the information using __str__ method
# Person's name is Mr X
# Address is Bristol
# Now setting the names and address
# Printing the information using __str__ method
# Person's name is Abdur Rakib
# Address is UWE Frenchay Campus 4QXX
# Creating another Person object by passing the values explicitly
# Printing the information using __str__ method
# Person's name is Jun Hong
# Address is UWE Frenchay Campus 3QXX