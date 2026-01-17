# Parameterised constructor and object creation by passing value
# Practical 7 - Exercise 1 - Task 1.5
# Nirvik K.C.

class Kitten:
    # constructor 
    # def __init__(self): 
    # initilialising instance/member variable age 
    #   self.age = 1
    # Parametrised constructor
    def __init__(self, age):
        # Initialising instance/ member variable age
        self.age = age

    # Instance/member method
    def display_age(self):
        print(self.age)

# Creating object by passing a value to the parametrised constructor
kitt = Kitten(3)

# # Calling the instance/member method using the object kitt
kitt.display_age()

# Output: 3
