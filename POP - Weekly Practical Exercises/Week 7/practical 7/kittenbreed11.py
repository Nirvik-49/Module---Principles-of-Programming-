# Introduction of the class variable and printing its value -  breed value has been changed to American Bobtail
# Practical 7 - Exercise 2 - Task 2.1 (b)
# Nirvik K.C.

class Kitten:
    # Class variable which is shared by all instances of the Kitten class
    # breed value - Abyssinian
    breed = 'Abyssinian'

    # Parameterized constructor
    def __init__(self, value):
        # initilialising instance/member variable age
        self.age = value

    # An instance/member method 
    def set_age(self, value):
        self.age = value

    # An instance/member method
    def display_age(self):
        print(self.age)

# Create two kitten objects using parameterized constructor
kitt = Kitten(3)
kitt2 = Kitten(4)

# Display the inital ages
kitt.display_age()  
kitt2.display_age()  
kitt.display_age()  

# Change the age of kitt using setter method
kitt.set_age(5)
kitt.display_age()

# Print the class variable breed
print(kitt.breed)
print(kitt2.breed)
print(Kitten.breed)

# print(Kitten.age) # instance variable cannot be accessed via Class. 
# It would raise AttributeError

# Modify the class variable
Kitten.breed = 'American Bobtail'

# Print the change in variable
print(kitt.breed)
print(kitt2.breed)

# Output:
# 3
# 4
# 3
# 5
# Abyssinian
# Abyssinian
# Abyssinian
# American Bobtail
# American Bobtail