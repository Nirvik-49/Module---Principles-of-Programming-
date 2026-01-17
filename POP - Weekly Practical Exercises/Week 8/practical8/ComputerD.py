# Create an array of objects to represent information about the objects on the list
# Practical 8 - Exercise 1 (Task 1.7)
# Nirvik K.C

class ComputerD:
    # Parameterized constructor
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    # Getters
    def getName(self):
        return self.__name
    
    def getPrice(self):
        return self.__price
    
    # Display method - using getters to access the variables
    def display(self):
        print(f"Computer's name is: {self.getName()} and its price is: {self.getPrice()}")

# Create an empty list to store 5 computers
object_list = []

print("Enter details for 5 computers:")

# Use loop 5 times to get input for each computer
for i in range(5):
    print(f"Computer {i+1}:")

    # User provides a valid computer name
    isValidName = False
    while not isValidName:
        computername = input("Enter computer's name: ")
        if 2 <= len(computername) <= 10:
            isValidName = True
        else:
            print("You must enter a valid name between 2 and 10 characters long")

    # User provides a valid computer price
    isValidPrice = False
    while not isValidPrice:
        computerprice = float(input("Enter computer's price: "))
        if 99.99 <= computerprice <= 999.99:
            isValidPrice = True
        else:
            print("You must enter a valid price between 99.99 and 999.99")

    # appending class instances to list  
    object_list.append(ComputerD(computername,computerprice)) 


# Displaying computer's information 
for obj in object_list: 
    obj.display()

# Output:
# Enter details for 5 computers:
# Computer 1:
#Enter computer's name: HP
# Enter computer's price: 378.89
# Computer 2:
# Enter computer's name: Dell
# Enter computer's price: 490.90
# Computer 3:
# Enter computer's name: Lenovo
# Enter computer's price: 308.78
# Computer 4:
# Enter computer's name: Mac
# Enter computer's price: 986.78
# Computer 5:
# Enter computer's name: Asus
# Enter computer's price: 234.56
# Computer's name is: HP and its price is: 378.89
# Computer's name is: Dell and its price is: 490.9
# Computer's name is: Lenovo and its price is: 308.78
# Computer's name is: Mac and its price is: 986.78
# Computer's name is: Asus and its price is: 234.56