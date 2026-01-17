# Testing protected member variable with single underscore
# Practical 9 - Exercise 1 - Task 1.5 (b)
# Nirvik K.C.

class Shape:
    # Constructor - change the access modifier of  “colour” variable
    def __init__(self, colour = 'Black'):
        # (b) Protected attributes - use of single underscore
        self._colour = colour
        print("Shape constructor is called")

        # (a) Private attributes - use of double underscore
        # self.__colour = colour
        # print("Shape constructor is called")

    def displayShape(self):
        print("Shape is displaying")

    # Public getter used to read the protected variable
    def getColour(self):
        return self._colour

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        print("Rectangle constructor is called")

    def displayRectangle(self):
        print("Rectangle is displaying")

    # Method which accessed the protected variable 'colour' directly
    def getRectangleColour(self):
        return self._colour
    
# Create Rectangle object
rec = Rectangle()

# Using inherited method
rec.displayShape()

# Using Rectangle's own method
rec.displayRectangle()

# Print the colour
print("Colour: ", rec.getRectangleColour())

# Direct access of the private attributes does not change the value
rec._colour = "Red"

# Print the colour after change - Still Black
print("New Colour: ", rec.getRectangleColour())

# Output:
# Shape constructor is called
# Rectangle constructor is called
# Shape is displaying
# Rectangle is displaying
# Colour:  Black
# New Colour: Red 