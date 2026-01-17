# Modify kitten8.py code - commented statement kitt3 = Kitten() and introduction and calling of a new member method set_age
# Practical 7 - Exercise 1 - Task 1.9
# Nirvik K.C.

class Kitten:
    # Parameterized constructor
    def __init__(self, value):
        # Initialising instance/member variable age with passed value
        self.age = value

    # An instance/member method to change variable age after creation
    def set_age(self, value):
         self.age = value

    # An Instance/member to display the age
    def display_age(self):
        print(self.age)

# Creating object of the class. This invokes parameterised constructor
kitt = Kitten(3)
kitt2 = Kitten(4)

# This invokes default constructor
# Commented out as it caused error
# kitt3 = Kitten()

# Calling the instance/member method using the object kitt

kitt.display_age()

kitt2.display_age()

kitt.display_age()

# Change the age of kitt using the new set_age method
kitt.set_age(5)

# Display the age after the change
kitt.display_age()

# Output:
# 3
# 4
# 3
# 5

# Difference between parameterised (or default) constructor ( __init__ ) and Setter Method like (set_age)

# 1. Constructor runs automatically only once when object is created.
# 1. Setter is called manually whenever you want to change the value later

# 2. Constructor is ideal for required initial values/initialisation.
# 2. Setter is ideal for optional or future changes made to an object's attributes after the object has already been created.

# 3. Constructor cannot be called again after creation.
# 3. Setter can be called multiple times.

# 4. Constructor usually has no validation logic, just set the value.
# 4. Setter can include validation, logic, etc.