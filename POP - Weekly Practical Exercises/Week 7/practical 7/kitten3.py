# Python - Member variable, method, and constructor
# Practical 7 - Exercise 1 - Task 1.3
# Nirvik K.C.

class Kitten:
    # Constructor (default constructor - no arguments)
    def __init__(self):
        # Initialise instance/member variable 'age'
        self.age = 1

        # An instance/member method
    def display_age(self):
        print(self.age)

# Creating object of the class
kitt = Kitten()

# Calling the method using the object
kitt.display_age()

# Output: 1