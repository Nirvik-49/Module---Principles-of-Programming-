# Call the method using the object created and run your program
# Practical 7 - Exercise 1 - Task 1.7
# Nirvik K.C.

class Kitten:
    # Parameterised constructor
    def __init__(self, value):
        # Initialising instance/member variable age
        self.age = value

    # Instance/member method
    def display_age(self):
        print(self.age)

# Creating objects of the class. This invokes parametrised constructor
kitt = Kitten(3)
kitt2 = Kitten(4)

# Calling the method 'display_age()' on both objects
kitt.display_age()
kitt2.display_age()

# Calling display_age() again on the object kitt
kitt.display_age() # Prints 3 again

# Output:
# age = 3
# age = 4
# age = 3