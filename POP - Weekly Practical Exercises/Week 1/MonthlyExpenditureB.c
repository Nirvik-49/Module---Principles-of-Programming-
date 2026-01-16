/* Print monthly expenditure
Practical 1, Part 2 (b)
Nirvik K.C. */

/* Edit the program MonthlyExpenditureA to MonthlyExpenditureB to calculate the total money spent last month on food, leisure, and clothes.
Also, replaces those default values from the previous program with your own. */

#include <stdio.h>
int main()
{
    float foodExpenses = 350.00;
    float leisureExpenses = 175.00;
    float clothesExpenses = 100.00;
    float totalSpent;
    totalSpent = foodExpenses + leisureExpenses + clothesExpenses;
    printf("\nThe total expenditure this month was £%.2f.\n", totalSpent);
    return 0;
}

// Output : The total expenditure this month was £625.00.