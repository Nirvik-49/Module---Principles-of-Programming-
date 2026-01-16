/* Print monthly expenditure
Practical 1, Part 2 (a)
Nirvik K.C. */

// Type the following code in MonthlyExpenditureA.
// Code:
/*  define variables and assign values to them
    float foodExpenses = 300.0; //variable for food expenses
    float leisureExpenses = 100.0; //assign 100.0 to leisureExpenses
    float clothesExpenses = 50.0;
    float totalSpent; //variable for total expenses

    totalSpent = foodExpenses + leisureExpenses + clothesExpenses;

    printf("The total expenditure this month was £%.2f\n\n", totalSpent); */

#include <stdio.h>
int main()
{
    float foodExpenses = 300.00;
    float leisureExpenses = 100.00;
    float clothesExpenses = 50.00;
    float totalSpent;
    totalSpent = foodExpenses + leisureExpenses + clothesExpenses;
    printf("The total expenditure this month was £%.2f.\n", totalSpent);
    return 0;
}

// Output : The total expenditure this month was £450.00.