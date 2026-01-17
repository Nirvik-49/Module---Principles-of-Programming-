# Use of Polymorphism: overriding method
# Practical 9 - Exercise 1 - Task 1.7
# Nirvik K.C.

class Shape:
    # Constructor for Shape Class
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

    def display(self):
        print("Rectangle is displaying")

    def getRectangleColour(self):
        return self.getColour()
    

# Create Rectangle object
rec = Rectangle()

# Print the colour using getter
print(rec.getRectangleColour())

# Call display() on Rectangle object
rec.display()

# Output:
# Shape constructor is called
# Rectangle constructor is called
# Black
# Rectangle is displaying

# Explanation of output order and why "Rectangle is displaying" is shown (not "Shape is displaying")
# Reason: This is an example of method overriding in polymorphism.
# The Rectangle class inherits from Shape and overrides the display() method.
# When rec.display() is called on a Rectangle object, Python looks for the method in the Rectangle class first.
# Since Rectangle has its own display() method, it executes that instead of the one in Shape.
# This is why "Rectangle is displaying" is printed instead of "Shape is displaying."
