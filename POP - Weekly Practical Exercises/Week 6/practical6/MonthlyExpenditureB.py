# Monthly Expenditure Calculator
# Practical 6, Part 2 (b) Monthly Expenditure
# @Nirvik K.C.

# define float variables and assign values to them
foodExpenses = 300.0    # assign 300.0 to foodExpenses 
leisureExpenses = 100.0 # assign 100.0 to leisureExpenses 
clothesExpenses = 50.0  # assign 50.0 to clothesExpenses

# new variables for accommodation and travel should be of type integer
accomodationExpenses = 1500     # assign 1500 to accomodation
travelExpenses = 200    # assign 200 to travelExpenses

totalSpent = 0.0        # assign float variable for total expenses, initialised to 0.0

# Calculate the total expenses
totalSpent = (foodExpenses + leisureExpenses + clothesExpenses + accomodationExpenses + travelExpenses)

# Display the result
print("The total expenditure this month was: ", totalSpent)

# Output: The total expenditure this month was:  2150.0