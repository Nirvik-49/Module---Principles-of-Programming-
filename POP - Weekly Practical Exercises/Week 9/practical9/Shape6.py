# Testing private variable (double underscore) in inheritance
# Practical 9 - Exercise 1 - Task 1.5 (a)
# Nirvik K.C.

class Shape:
    # Constructor - change the access modifier of  “colour” variable 
    def __init__(self, colour='Black'):
        # (a) Private attributes - use of double underscore
        self.__colour = colour
        print("Shape constructor is called")

        # (b) Protected version - use of single underscore
        # self._colour = colour
        # print("Shape constructor is called")
    
    def displayShape(self):
        print("Shape is displaying")

    # Public getter method read the private variable
    def getColour(self):
        return self.__colour
    
class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        print("Rectangle constructor is called")

    def displayRectangle(self):
        print("Rectangle is displaying")

    # This method tries to access colour
    def getRectangleColour(self):
        # Direct access to private variable using parent's public getter
        return self.getColour()
    
# Create Rectangle object
rec = Rectangle()

# Using inherited method
rec.displayShape()

# Using Rectangle's own method
rec.displayRectangle()

# Print the colour
print("Colour: ", rec.getRectangleColour())

# Direct access of the private attributes does not change the value
rec.__colour = "Red"

# Print the colour after change - Still Black
print("New Colour: ", rec.getRectangleColour())


# Output:
# Shape constructor is called
# Rectangle constructor is called
# Shape is displaying
# Rectangle is displaying
# Colour:  Black
# New Colour: Black