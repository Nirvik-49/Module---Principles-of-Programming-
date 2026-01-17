# Access the list items by referring to the index number
# Practical 6, Part 4 - Exercise 6
# @Nirvik K.C.

# Using the already defined months list
months = []
index = 0

# Loop through the list using index
while index < 12:
    m = input("Enter a month: ")
    months.append(m)  # Append the user input to the months list
    index += 1        # Increment the index

print("\nNow printing the months you entered\n")
for x in months:
    print(x)  # print each month in the list

# Output: Prints the months entered by the user