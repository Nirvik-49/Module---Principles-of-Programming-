# Monthly Expenditure Calculator
# Practical 6, Part 2 (c) Monthly Expenditure, take input from the keyboard
# @Nirvik K.C.

# Prompt the user and take input from the user for food expenses
foodExpenses = float(input("Enter food expenses: "))

# Prompt the user and take input from the user for leisure expenses
leisureExpenses = float(input("Enter leisure expenses: "))

# Prompt the user and take input from the user for clothes expenses
clothesExpenses = float(input("Enter clothes expenses: "))

# Prompt the user and take input from the user for accommodation expenses
accomodationExpenses = int(input("Enter accommodation expenses: "))

# Prompt the user and take input from the user for travel expenses
travelExpenses = int(input("Enter travel expenses: "))

totalSpent = 0.0        # assign float variable for total expenses, initialised to 0.0

# Calculate the total expenses
totalSpent = (foodExpenses + leisureExpenses + clothesExpenses + accomodationExpenses + travelExpenses)

# Display the result
print("The total expenditure this month was: ", totalSpent)

# Output:
# Enter food expenses: 350.50
# Enter leisure expenses: 150.00
# Enter clothes expenses: 85.00
# Enter accommodation expenses: 10000
# Enter travel expenses: 1500
# The total expenditure this month was:  12085.5
