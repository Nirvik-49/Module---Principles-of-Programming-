# Public member variables (direct access/modification)
# Practical 8 - Exercise 1 (Task 1.3)
# Nirvik K.C.

class ComputerA:
    # Parameterized constructor
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Using setters method
    def setName(self, name):
        self.name = name

    # Using getters
    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
    
    # Display the current name and price of the Computer
    # An instance/member method 
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
comp = ComputerA(computername, computerprice)

# displaying computer's information 
comp.display() 

# setting a different computer name using the setName method 
# comp.setName("Dell")

# setting a different computer name by accessing the name variable which is public 
comp.name = 'Dell'

# setting new price using the setPrice method 
# comp.setPrice(890.90)

#setting new price by accessing the price variable which is public 
comp.price = 890.90

# Displaying computer's (new) information
comp.display()

# Output:
# Enter computer's name: HP
# Enter computer's price: 199.99
# Computer's name is: HP and its price is: 199.99
# Computer's name is: Dell and its price is: 890.9