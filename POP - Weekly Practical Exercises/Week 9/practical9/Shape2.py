# Showing constructors in inheritance
# Practical 9 - Exercise 1 (Task 1.2)
# Nirvik K.C.

class Shape:
    # Constructor for Shape class
    def __init__(self):
        print("Shape constructor is called")

    def displayShape(self):
        print("Shape is displaying")

class Rectangle(Shape):
    # Constructor for the class Rectangle
    def __init__(self):
        print("Rectangle constructor is called")

    def displayRectangle(self):
        print("Rectangle is displaying")

# Create objects of Rectangle class
rec = Rectangle()

# Call the methods
rec.displayShape()
rec.displayRectangle()

# Output:
# Rectangle constructor is called
# Shape is displaying
# Rectangle is displaying