/* Print monthly expenditure
Practical 1, Part 2 (e)
Nirvik K.C. */

/* Edit and save the MonthlyExpenditureD.c to MonthlyExpenditureE.c to spend a fixed amount on the accommodation expenses each month.
Make the required change in the program so that the accommodation expenses are represented as a constant. */
#include <stdio.h>
int main()
{
    float foodExpenses;
    float leisureExpenses;
    float clothesExpenses;
    float travelExpenses;
    // Define accommodation expense as a constant
    const float ACCOMMODATION_EXPENSES = 500.00;
    float totalSpent;
    // To take input from the user
    printf("\nEnter the food expenses: ");
    scanf("%f", &foodExpenses);
    printf("\nEnter the leisure expenses: ");
    scanf("%f", &leisureExpenses);
    printf("\nEnter the clothes expenses: ");
    scanf("%f", &clothesExpenses);
    // Accommdation expenses are fixed so no input needed
    printf("\nEnter the travel expenses: ");
    scanf("%f", &travelExpenses);

    // Calculate the total expenses
    totalSpent = foodExpenses + leisureExpenses + clothesExpenses + ACCOMMODATION_EXPENSES + travelExpenses;

    // Display the total expenses in the terminal
    printf("\nThe total expenditure for this month was £%.2f.\n", totalSpent);
    return 0;
}

// Output : The total expenditure for this month was £1320.00.