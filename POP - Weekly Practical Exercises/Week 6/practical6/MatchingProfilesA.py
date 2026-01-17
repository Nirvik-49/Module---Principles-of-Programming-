# DNA Profile Matching - Identify a repeated offender
# Practical 6, Part 4 - Exercise 7
# @Nirvik K.C.

# Two empty lists to store DNA profiles of Suspects and Criminal
suspect_profiles = []
criminal_profiles = []

# Enter DNA profiles for Suspect
print("Enter the 10 DNA profile values of the Suspect: ")
for i in range(10):
    suspect_gene = (float(input(f"Enter suspect chromosome {i+1} value: ")))
    suspect_profiles.append(suspect_gene)

# Enter DNA profiles for Criminal
print("\nEnter the 10 DNA profile values of the Criminal: ")
for i in range(10):
    criminal_gene = float(input(f"Enter criminal chromosome {i+1} value: "))
    criminal_profiles.append(criminal_gene)

# Compare DNA profiles

print("\nSuspect DNA profile :",suspect_profiles)
print("\nCriminal DNA profile :", criminal_profiles)

if suspect_profiles == criminal_profiles:
    print("\nThe profiles match. The suspect is a repeated offender.")
else:
    print("\nThe profiles do not match.")

