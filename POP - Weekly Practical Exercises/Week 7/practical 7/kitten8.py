# Create another object kitt3 without passing any value
# Practical 7 - Exercise 1 - Task 1.8
# Nirvik K.C.

class Kitten:
    # Parameterized constructor
    def __init__(self, value):
        # Initialising instance/member variable age
        self.age = value

    # Instance/member method
    def display_age(self):
        print(self.age)

# creating object of the class. This invokes parameterised constructor 
kitt = Kitten(3)
kitt2 = Kitten(4)

# This invokes parameterised constructor
# Create a third object without passing any value
kitt3 = Kitten()

# Calling the instance/member method
kitt.display_age()

kitt2.display_age()

kitt.display_age()

# When you run the program, you get an error. TypeError: Kitten.__init__() missing 1 required positional argument: 'value'