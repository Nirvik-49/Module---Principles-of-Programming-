# Using super() to call parent constructor
# Practical 9 - Exercise 1 (Task 1.3)
# Nirvik K.C.

class Shape:
    # Constructor for Shape class
    def __init__(self):
        print("Shape constructor is called")

    def displayShape(self):
        print("Shape is displaying")

class Rectangle(Shape):
    # constructor for Rectangle class, Base class constructor is called using 'super' 
    def __init__(self):
        super().__init__()

        print("Rectangle constructor is called")

    def displayRectangle(self):
        print("Rectangle is displaying")

# Create a Rectangle object
rec = Rectangle()

# Call the methods
rec.displayShape()
rec.displayRectangle()

# Output:
# Shape constructor is called
# Rectangle constructor is called
# Shape is displaying
# Rectangle is displaying

# Explanation of the output:

# First line of the output: "Shape constructor is called"
# Reason: Because inside the Rectangle.__init(), we wrote super().__init__() which tell Python to first run the parent's constructor.

# Second line of the output: "Rectangle constructor is called"
# Reason: The rest of Rectangle.__init__() after super() finished

# Third line of the output: "Shape is displaying"
# Reason: It is called from rec.displayShape() where displayShape() exits in the parent class (Shape). Class Rectangle inherited it, so it can be called on Rectangle objects

# Fourth line of the output: "Rectangle is displaying"
# Reason : This line is called from rec.displayRectangle(). The method is present in the Rectangle class, not Shape.