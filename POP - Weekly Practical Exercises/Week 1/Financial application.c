/* Calculate account value after the certain time
Practical 1, Part 3 (c)
Nirvik K.C. */

/* Write a program that prompts the user to enter a monthly savings amount and displays the
account value after the sixth month. */
/* Account value compounded monthly at an annual interest rate of 5%. */
#include <stdio.h>
int main()
{
    float monthly_saving;
    float interest_rate = 0.05;
    float monthly_interest_rate = interest_rate / 12;

    // To take input- monthly saving value from the user.

    printf("\nEnter the monthly saving amount: ");
    scanf("%f", &monthly_saving);
    float month1 = monthly_saving * (1 + monthly_interest_rate);
    float month2 = (monthly_saving + month1) * (1 + monthly_interest_rate);
    float month3 = (monthly_saving + month2) * (1 + monthly_interest_rate);
    float month4 = (monthly_saving + month3) * (1 + monthly_interest_rate);
    float month5 = (monthly_saving + month4) * (1 + monthly_interest_rate);
    float month6 = (monthly_saving + month5) * (1 + monthly_interest_rate);

    // Display the output
    printf("\nAccount value after the sixth month: $%.2f.\n", month6);
    return 0;
}

/*
Output :
Enter the monthly saving amount: 100

Account value after the sixth month: $608.81.
 */