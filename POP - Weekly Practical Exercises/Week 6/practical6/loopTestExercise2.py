# Printing months from a list using a for loop 
# Practical 6, Part 4 - Exercise 2
# @Nirvik K.C.

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
for x in months:
    if x == "Apr":
        continue
    print(x)  # continue statement skips the print(x) line for the month of April

# Output:
# Jan
# Feb
# Mar
# May
# Jun
# Jul
# Aug
# Sep
# Oct
# Nov
# Dec