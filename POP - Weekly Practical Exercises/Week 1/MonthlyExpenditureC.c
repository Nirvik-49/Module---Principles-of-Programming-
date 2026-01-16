/* Print monthly expenditure
Practical 1, Part 2 (c)
Nirvik K.C. */

/* Edit and extend the MonthlyExpenditureB to MonthlyExpenditureC program to calculate the total money spent last month on food, leisure, clothes, accommodation, and travel.
Also, add default values for the new variables (accommodation and travel). */
#include <stdio.h>
int main()
{
    float foodExpenses = 350.0;
    float leisureExpenses = 175.00;
    float clothesExpenses = 100.00;
    float accommodationExpenses = 600.00;
    float travelExpenses = 150.00;
    float totalSpent;
    // Calculate the total expenses
    totalSpent = foodExpenses + leisureExpenses + clothesExpenses + accommodationExpenses + travelExpenses;
    printf("\nThe total expenditure this month was £%.2f.\n", totalSpent);
    return 0;
}

// Output : The total expenditure this month was £1375.00.