# Create object kitt2 by passing the value 4, call the member method, display_age(), and run your program. 
# Practical 7 - Exercise 1 - Task 1.6
# Nirvik K.C.

class Kitten:
    # Parameterised constructor
    def __init__(self, value):
        # Initialising instance/member variable age
        self.age = value

    # Instance/member method
    def display_age(self):
        print(self.age)

# Creating first object of the class. This invokes parameterised constructor
kitt = Kitten(3)

# Creating object of the class. This invokes parameterised constructor
kitt2 = Kitten(4)

# Calling the instance/member method using the object kitt
kitt.display_age()

kitt2.display_age()

# Output:
# 3
# 4