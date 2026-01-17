# Python - No use of any explicit constructor
# Practical 7 - Exercise 1 - Task 1.4
# Nirvik K.C.

class Kitten:
    # constructor
    # def __init__(self):
    #     # Initialising instance/member variable age
    #     self.age = 1

    # An instance/member method
    def display_age(self):
        print("Age unknown")

# Creating object of the class. This invoked constructor
kitt = Kitten()

# Calling the method using the object
kitt.display_age()

# Output: Age unknown