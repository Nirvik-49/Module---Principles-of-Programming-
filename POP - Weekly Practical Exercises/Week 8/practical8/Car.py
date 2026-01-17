# UML to Code : Class Car
# Practical 8 - Exercise 2
# Nirvik K.C

class Car:
    def __init__(self, brand, fuelLevel):
        self.__brand = brand
        self.__fuelLevel = 0.0
        self.setFuelLevel(fuelLevel)
    
    # Getters
    def getBrand(self):
        return self.__brand
    
    def setBrand(self, brand):
        return self.__fuelLevel
    
    def getFuelLevel(self):
        return self.__fuelLevel
    
    # Setters
    def setBrand(self, brand):
        self.__brand = brand

    # Fuel level of the Car    
    def setFuelLevel(self, level):
        level = float(level)

        if level < 0.0:
            self.__fuelLevel = 0.0
        elif level > 100.0:
            self.__fuelLevel = 100.0
        else:
            self.__fuelLevel = level

    # Refuel the car
    def refuel(self, amount):
        print(f"Adding {amount} litre of fuel to {self.__brand}")
        self.setFuelLevel(self.__fuelLevel + amount)

    def display(self):
        print(f"Car info: Brand: {self.__brand} and Fuel Level: {self.__fuelLevel}%")

# Displaying Car's Info
my_car = Car("Toyota", 55.5)
my_car.display()

my_car.refuel(65.0)
my_car.display()

# Output:
# Car info: Brand: Toyota and Fuel Level: 55.5%
# Adding 65.0 litre of fuel to Toyota
# Car info: Brand: Toyota and Fuel Level: 100.0%