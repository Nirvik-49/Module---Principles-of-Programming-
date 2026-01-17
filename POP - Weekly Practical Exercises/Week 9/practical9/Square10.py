# Polymorphism & calling subclass method on unrelated object
# Practical 9 - Exercise 1 - Task 1.9
# Nirvik K.C.

class Shape:
    # Constructor for Shape class
    def __init__(self, colour='Black'):
        self.colour = colour
        print("Shape constructor is called")

    def display(self):
        print("Shape is displaying")

    def getColour(self):
        return self.colour
    
class Rectangle(Shape):
    # Constructor for Rectangle class
    def __init__(self):
        super().__init__()
        print("Rectangle constructor is called")

    # Overrides the display() method from Shape
    def display(self):
        print("Rectangle is displaying")

    def getRectangleColour(self):
        return self.getColour()
    
class Square(Shape):
    # Empty body with no constructor or method defined
    # Inherits everything from Shape class
    pass

# Create a Rectangle object
rec = Rectangle()

# Call the getRectangleColour() method of the rectangle class 
print(rec.getRectangleColour())

# Call display() on Rectangle object - uses Rectangle's overridden method
rec.display()

# Create a Square object
sqr = Square()

# Call display() on Square object - inherits method from Shape
sqr.display()

# Call method - getRectangleColour() on Square object
sqr.getRectangleColour()

# Output(until the error):
# Shape constructor is called
# Rectangle constructor is called
# Black
# Rectangle is displaying
# Shape constructor is called
# Shape is displaying
# AttributeError: 'Square' object has no attribute 'getRectangleColour'