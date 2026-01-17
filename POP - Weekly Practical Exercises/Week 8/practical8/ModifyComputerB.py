# Private member variables accessed via public methods
# Practical 8 - Exercise 1 (Task 1.5)
# Nirvik K.C.

class ComputerB:
    # Parameterized constructor
    def __init__(self, name, price):
        # Private instance variables (Using double underscore)
        self.__name = name
        self.__price = price

    # Using Setters - public methods to change private variables
    def setName(self, name):
        self.__name = name
    
    def setPrice(self, price):
        self.__price = price

    # Using Getters - public methods to read private variables
    def getName(self):
        return self.__name
    
    def getPrice(self):
        return self.__price
    
    # Display method - using getters to access the variables
    def display(self):
        print(f"Computer's name is: {self.getName()} and its price is: {self.getPrice()}")

# User provides a valid computer name
isValidName = False
while not isValidName:
    computername = input("Enter computer's name: ")

    if 2 <= len(computername) <= 10:
        isValidName = True
    else:
        print("You must enter a value name between 2 and 10 characters long")
    
# User provides a valid computer price
isValidPrice = False
while not isValidPrice:
    computerprice = float(input("Enter computer's price: "))
    if 99.99 <= computerprice <= 999.99:
        isValidPrice = True
    else:
        print("You must enter a valid price between 99.99 and 999.99")

# Creating the comp object based on user's input 
comp = ComputerB(computername, computerprice)

# Displaying computer's information 
comp.display() 

# Setting a different computer name using the setName method 
comp.setName("Dell") 

# Setting a different computer name by accessing the name variable which is public 
# comp.__name = 'Dell' 

# Setting new price using the setPrice method 
comp.setPrice(890.90) 

# Setting new price by accessing the price variable which is public 
# comp.__price = 890.90 

# Displaying computer's (new) information 
comp.display()

# Output:
# Enter computer's name: HP
# Enter computer's price: 199.99
# Computer's name is: HP and its price is: 199.99
# Computer's name is: Dell and its price is: 890.9
