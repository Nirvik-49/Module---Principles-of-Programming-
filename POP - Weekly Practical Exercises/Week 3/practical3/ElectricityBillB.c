/* read values from input file
Practical 3, Part 2
@Nirvik K.C. */

#include <stdio.h>
FILE *fp; // define a file pointer for the file to hold a disk location
int main()
{
    // open file for reading
    fp = fopen("bill_input.txt", "r");
    if (fp == NULL)
    {
        printf("Error opening the file");
        return 1;
    }

    // Declare variables to store input values
    int previous, current, day, month;
    int units;

    printf("Starting validation of electricity bill readings from the file\n\n");
    // Loop to read set of input values from the file
    for (int i = 1; i <= 7; i++)
    {
        printf("The Electricity Bill Set %d\n", i);
        fscanf(fp, "%d %d %d %d", &previous, &current, &day, &month);

        // Display the read values
        printf("Input read: Previous Reading= %d, Current Reading= %d, Day= %d, Month= %d\n", previous, current, day, month);

        // Validation checks
        if (current < 0 || current > 9999)
        {
            printf("Error: Current meter reading out of range (0-9999)\n");
        }

        if (previous < 0 || previous > 9999)
        {
            printf("Error: Previous meter reading out of range (0-9999)\n");
        }

        if (current - previous > 1000)
        {
            printf("Error: Electricity used more than 1000 units\n");
        }

        if (previous > current)
        {
            printf("Error: Previous reading is greater than current reading\n");
        }

        if (month < 1 || month > 12)
        {
            printf("Error: Month out of range (1-12)\n");
        }

        // Check days in month
        if ((month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) && (day < 1 || day > 31))
        {
            printf("Error: Day out of range for the given month (1-31)\n");
        }

        if ((month == 4 || month == 6 || month == 9 || month == 11) && (day < 1 || day > 30))
        {
            printf("Error: Day out of range 1 to 30\n");
        }

        if (month == 2 && (day < 1 || day > 29))
        {
            printf("Error: Day out of range 1 to 29\n");
        }
        printf("\n");
    }
    fclose(fp); // Closes the file
    return 0;
}

/* Output :
Starting validation of electricity bill readings from the file

The Electricity Bill Set 1
Input read: Previous Reading= 900, Current Reading= 800, Day= 23, Month= 5
Error: Previous reading is greater than current reading

The Electricity Bill Set 2
Input read: Previous Reading= 9000, Current Reading= 9999, Day= 12, Month= 2

The Electricity Bill Set 3
Input read: Previous Reading= 9999, Current Reading= 10005, Day= 14, Month= 6
Error: Current meter reading out of range (0-9999)

The Electricity Bill Set 4
Input read: Previous Reading= 500, Current Reading= 6000, Day= 26, Month= 7
Error: Electricity used more than 1000 units

The Electricity Bill Set 5
Input read: Previous Reading= 10000, Current Reading= 10100, Day= 10, Month= 9
Error: Current meter reading out of range (0-9999)
Error: Previous meter reading out of range (0-9999)

The Electricity Bill Set 6
Input read: Previous Reading= 6000, Current Reading= 6890, Day= 30, Month= 2
Error: Day out of range 1 to 29

The Electricity Bill Set 7
Input read: Previous Reading= 590, Current Reading= 829, Day= 31, Month= 9
Error: Day out of range 1 to 30
*/