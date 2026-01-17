# Design and implement Car class with data fields, constructor, methods, getters and setters
# Practical 7 - Exercise 4
# Nirvik K.C.

class Car:
    def __init__(self, doors, price, color, brand):
        """Constructor to initialise the attributes of the car"""
        self.doors = doors
        self.price = price
        self.color = color
        self.brand = brand

    # Methods for starting the car and stopping the car
    def startCar(self):
        print("Car has started")

    def stopCar(self):
        print("Car has stopped")

    # Using getter methods
    def getNumberOfDoors(self):
        return self.doors
    
    def getPrice(self):
        return self.price
    
    def getColor(self):
        return self.color
    
    def getBrand(self):
        return self.brand
    
    # Using setter methods
    def setNumberOfDoors(self, doors):
        self.doors = doors

    def setPrice(self, price):
        self.price = price
    
    def setColor(self, color):
        self.color = color

    def setBrand(self, brand):
        self.brand = brand


# Create object for the Car
car_details = Car(5, 20000, "White", "ToyCar")

# Display the initial values using getters
print("Initial Car Details:")
print(f"Brand: {car_details.getBrand()}")
print(f"Doors: {car_details.getNumberOfDoors()}")
print(f"Price: {car_details.getPrice()}")
print(f"Color: {car_details.getColor()}")
print()

# To start and stop the car
car_details.startCar()
car_details.stopCar()
print()

# Change the attributes using setters
print("Updating new details for the Car")
car_details.setPrice(25000)
car_details.setColor("Red")
car_details.setBrand("SpeedToy")


# Display updated values
print("Updated Car details:")
print(f"New Brand: {car_details.getBrand()}")
print(f"New Price: {car_details.getPrice()}")
print(f"New Color: {car_details.getColor()}")
print()

# Start and stop the new car
car_details.startCar()
car_details.stopCar()
print()

# Output:
# Initial Car Details:
# Brand: ToyCar
# Doors: 5
# Price: 20000
# Color: White

# Car has started
# Car has stopped

# Updating new details for the Car
# Updated Car details:
# New Brand: SpeedToy
# New Price: 25000
# New Color: Red

# Car has started
# Car has stopped