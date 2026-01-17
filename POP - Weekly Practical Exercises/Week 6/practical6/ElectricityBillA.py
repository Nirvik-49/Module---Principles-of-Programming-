# Monthly Expenditure Calculator
# Practical 6, Part 3 -  Selections, Relational Operators and Boolean expressions  
# @Nirvik K.C.

# Enter previous meter reading 
previousMeterReading = int(input("Enter the previous meter reading: "))
# Enter current meter reading
presentMeterReading = int(input("Enter the present meter reading: "))

# Enter the day of the meter reading 
day = int(input("Enter the day of the meter reading: "))

# Enter the month of the meter reading 
month = int(input("Enter the month of the meter reading (1-12): "))

# Display the input data
print(f"\n{previousMeterReading} {presentMeterReading} {day} {month}")

# Input validation
# current meter reading within range 0..9999 
if (previousMeterReading < 0 or previousMeterReading > 9999):
    print("Error: previous meter reading is out of range\n")

if (presentMeterReading < 0 or presentMeterReading > 9999):
    print("Error: present meter reading is out of range\n")

# Previous reading not greater than present reading
if (previousMeterReading > presentMeterReading):
    print("Error: previous meter reading is more than present meter reading\n")

# Electricity used not more than 1000
usage = presentMeterReading - previousMeterReading
if (usage > 1000):
    print("Error: electricity usage is more than 1000\n")

#  month in range 1..12
if (month < 1 or month > 12):
    print("Error: month is out of range (must be 1-12)\n")

# Check for months with 31 days
# days in month must be correct (Jan, March, May, July, Augest, October, December)
if month in [1, 3, 5, 7, 8, 10, 12]:
    if day < 1 or day > 31:
        print("Error: day out of range for this month\n")

# Check 30 days in month must be correct (Apr, June, September, November)
elif month in [4, 6, 9, 11]:
    if day < 1 or day > 30:
        print("Error: day out of range for this month\n")

# Check seperately for February month
elif month == 2:
    if day < 1 or day > 29:
        print("Error: day out of range for February\n")   

# Enter the previous meter reading: 900
# Enter the present meter reading: 800
# Enter the day of the meter reading: 23
# Enter the month of the meter reading (1-12): 5

# 900 800 23 5
# Error: previous meter reading is more than present meter reading