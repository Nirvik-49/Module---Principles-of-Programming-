/* read values from input file
Practical 5 -  Part 3, 5.2 (Check password)
@Nirvik K.C. */

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

// Function to check password validity
int isValidPassword(const char *password)
{
    int length = strlen(password);

    // First rule: Must have at least 8 characters
    if (length < 8)
    {
        return false;
    }

    int digitCount = 0;

    // Check each character
    for (int i = 0; i < length; i++)
    {
        char ch = password[i];

        // Second Rule: Only letters and digits allowed
        if (!(
                (ch >= 'A' && ch <= 'Z') ||
                (ch >= 'a' && ch <= 'z') ||
                (ch >= '0' && ch <= '9')))
        {
            return false;
        }

        // Count the number of digits
        if (ch >= '0' && ch <= '9')
        {
            digitCount++;
        }
    }

    // Third Rule: Must contain at least two digits
    if (digitCount < 2)
    {
        return false;
    }
    else
    {
        return true; // password is valid
    }
}

int main()
{
    char password[100];

    printf("Enter a password: ");
    scanf("%s", password);

    if (isValidPassword(password))
    {
        printf("The password is valid.\n");
    }
    else
    {
        printf("The password is invalid.\n");
    }
    return 0;
}

/*Output:
Enter a password: 12345678
The password is valid.

Enter a password: Valid123
The password is valid.

Enter a password: Password1
The password is invalid.
*/