# DNA Profile Matching - Identify a repeated offender with Function
# Practical 6, Part 4 - Exercise 8
# @Nirvik K.C.

def matchingProfiles(suspect_dna, criminal_dna):
    # Th function compares the two list of DNA profiles and returns True if they match, otherwise False
    if suspect_dna == criminal_dna:
        return True
    else:
        return False
    
# Two empty lists to store DNA profiles of Suspects and Criminal
suspect_profiles = []
criminal_profiles = []

# Enter DNA profiles for Suspect
print("Enter the 10 DNA profile values of the Suspect: ")
for i in range(10):
    suspect_gene = float(input(f"Enter suspect chromosome {i+1} value: "))
    suspect_profiles.append(suspect_gene)

# Enter DNA profiles for Criminal
print("\nEnter the 10 DNA profile values of the Criminal: ")
for i in range(10):
    criminal_gene = float(input(f"Enter criminal chromosome {i+1} value: "))
    criminal_profiles.append(criminal_gene)


# The function to check the match 
is_repeated_offender = matchingProfiles(suspect_profiles, criminal_profiles)

# Display the result

print("\nSuspect DNA profile :",suspect_profiles)
print("\nCriminal DNA profile :", criminal_profiles)

if is_repeated_offender:
    print("\nThe profiles match. The suspect is a repeated offender.")
else:
    print("\nThe profiles do not match.")