/* Print monthly expenditure
Practical 1, Part 2 (d)
Nirvik K.C. */

/* Edit, extend and save the MonthlyExpenditureC to MonthlyExpenditureD program to take input from the keyboard, calculate total
money spent last month food, leisure, clothes, accommodation and travel, and display your total money on the screen. */
#include <stdio.h>
int main()
{
    float foodExpenses;
    float leisureExpenses;
    float clothesExpenses;
    float accommodationExpenses;
    float travelExpenses;
    float totalSpent;
    // To take input from the user
    printf("\nEnter the food expenses: ");
    scanf("%f", &foodExpenses);
    printf("\nEnter the leisure expenses: ");
    scanf("%f", &leisureExpenses);
    printf("\nEnter the clothes expenses: ");
    scanf("%f", &clothesExpenses);
    printf("\nEnter the accommodation expenses: ");
    scanf("%f", &accommodationExpenses);
    printf("\nEnter the travel expenses: ");
    scanf("%f", &travelExpenses);

    // Calculate the total expenses
    totalSpent = foodExpenses + leisureExpenses + clothesExpenses + accommodationExpenses + travelExpenses;

    // Display the total expenses in the terminal
    printf("\nThe total expenditure for this month was £%.2f.\n", totalSpent);
    return 0;
}
// Output : The total expenditure for this month was £1880.00.
