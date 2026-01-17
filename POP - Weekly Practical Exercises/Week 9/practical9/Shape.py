# Shape.py - Display the required shape
# Practical 9 - Exercise 1 (Task 1.1)
# Nirvik K.C.

class Shape:
    def displayShape(self):
        print("Shape is displaying")

# Class Rectangle inherits from Shape
class Rectangle(Shape):
    def displayRectangle(self):
        print("Rectangle is displaying")

# Create objects
rec = Rectangle()

# Call methods
rec.displayShape() 
rec.displayRectangle()

# Output:
# Shape is displaying
# Rectangle is displaying
