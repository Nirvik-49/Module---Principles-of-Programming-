# Implement a Rectangle class to display the width, height, area, and perimeter
# Practical 7 - Exercise 3
# Nirvik K.C.

class Rectangle:
    """
    A class created to represent a rectangle with width and height.
    A method named getArea() that returns the area of this rectangle.
    A method named getPerimeter() that returns the perimeter.
    """

    def __init__(self, width = 1.0, height = 1.0):
        # Constructor to create a rectangle.
        self.width = width   # width of the rectangle is 1.0
        self.height = height # height of the rectangle is 1.0

    def getArea(self):
        # Returns the area of the rectangle
        return self.width * self.height
    
    def getPerimeter(self):
        # Returns the perimeter of the rectangle
        return 2 * (self.width + self.height)
    

# Create the first rectangle object (width 4, height 40)
rect1 = Rectangle(4, 40)

# Create the second rectangle object (width 3.5, height 35.9)
rect2 = Rectangle(3.5, 35.9)

def display_rectangle(name, rect):
    print(f"{name}:")
    print(f"Width: {rect.width}")
    print(f"Height: {rect.height}")
    print(f"Area: {rect.getArea():.2f}")
    print(f"Perimeter: {rect.getPerimeter():.2f}")
    print()

# Display the width, height, area, and perimeter of both rectangles
display_rectangle("Rectangle 1", rect1)
display_rectangle("Rectangle 2", rect2)

# Output: 
# Rectangle 1:
# Width: 4
# Height: 40
# Area: 160.00
# Perimeter: 88.00

# Rectangle 2:
# Width: 3.5
# Height: 35.9
# Area: 125.65
# Perimeter: 78.80