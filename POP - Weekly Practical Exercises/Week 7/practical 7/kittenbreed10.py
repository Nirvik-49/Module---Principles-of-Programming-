# Introduction of the class variable and printing its value
# Practical 7 - Exercise 2 - Task 2.1 (a)
# Nirvik K.C.

class Kitten:
    # Class variable
    breed = 'Abyssinian'

    # Parameterized constructor
    def __init__(self, value):
        # Instance variable
        self.age = value

    # Instance method to change age
    def set_age(self, value):
        self.age = value

    # Instance method to display
    def display_age(self):
        print(self.age)

# Create objects using parameters constructor. This invokes parameterised constructor

kitt = Kitten(3)
kitt2 = Kitten(4)

# This invokes default constructor 
# kitt3 = Kitten() 

# Display initial ages using constructor
kitt.display_age()
kitt2.display_age()
kitt.display_age()

# Change age of the first kitten using the setter method
kitt.set_age(5)

# Show the new age
kitt.display_age()   # 5

# Print the class variable using both objects
print(kitt.breed)  # Abyssinia
print(kitt2.breed) # Abyssinia


# Output:
# 3
# 4
# 3
# 5
# Abyssinian
# Abyssinian