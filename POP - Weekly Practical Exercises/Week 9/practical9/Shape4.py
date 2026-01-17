# Accessing base public attribute in subclass
# Practical 9 - Exercise 1 (Task 1.4)
# Nirvik K.C.

class Shape:
    # constructor for Shape class 
    def __init__(self, colour='Black'):
        self.colour = colour
        print("Shape constructor is called")

    def displayShape(self):
        print("Shape is displaying")

    def getColour(self):
        return self.colour

class Rectangle(Shape):
     # constructor for Rectangle class
     #  Parent class constructor is called using super()
    def __init__(self):
         super().__init__()
         print("Rectangle constructor is called")

    def displayRectangle(self):
        print("Rectangle is displaying")

    def getRectangleColour(self):
        return self.colour    # accessed the public attribute from parent

# Create Rectangle object
rec = Rectangle()

# Print the colour which is accessed from the public attribute
print(rec.getRectangleColour())

# Output:
# Shape constructor is called 
# Rectangle constructor is called 
# Black