# Polymorphism & overriding with empty subclass
# Practical 9 - Exercise 1 - Task 1.8
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

# Call display() on Rectangle object - uses Rectangle's overridden method
rec.display()

# Create a Square object
sqr = Square()

# Call display() on Square object - inherits method from Shape
sqr.display()

        
# Output:
# Shape constructor is called
# Rectangle constructor is called
# Rectangle is displaying
# Shape constructor is called
# Shape is displaying