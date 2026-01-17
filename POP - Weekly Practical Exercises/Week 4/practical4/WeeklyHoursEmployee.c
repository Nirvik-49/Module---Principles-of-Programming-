/* Practical 4 - More Programming exercises, Part 4 - 4.4
   Compute the weekly hours for each employee
   @Nirvik K.C. */

#include <stdio.h>

int main()
{
    // 8 employees, 7 days
    int hours[8][7] = {
        {2, 4, 3, 4, 5, 8, 8},
        {7, 3, 4, 3, 3, 4, 4},
        {3, 3, 4, 3, 3, 2, 2},
        {9, 3, 4, 7, 3, 4, 1},
        {3, 5, 4, 3, 6, 3, 8},
        {3, 4, 4, 6, 3, 4, 4},
        {3, 7, 4, 8, 3, 8, 4},
        {6, 3, 5, 9, 2, 7, 9}};

    int total[8];
    int employeeOrder[8];
    int i, j, temp;
    int currentEmployee;

    // Calculate total hours for each employee
    for (i = 0; i < 8; i++)
    {
        total[i] = 0;
        for (j = 0; j < 7; j++)
        {
            total[i] = total[i] + hours[i][j];
        }
        employeeOrder[i] = i;
    }

    // Sort employees based on total hours
    for (i = 0; i < 7; i++)
    {
        for (j = 0; j < 7 - i; j++)
        {
            // Compare the totals using the current order
            if (total[employeeOrder[j]] < total[employeeOrder[j + 1]])
            {
                // Swap total hours
                temp = employeeOrder[j];
                employeeOrder[j] = employeeOrder[j + 1];
                employeeOrder[j + 1] = temp;
            }
        }
    }

    // Display result
    printf("Employee and their total weekly hours in decreasing order:\n");

    for (int k = 0; k < 8; k++)
    {
        currentEmployee = employeeOrder[k];
        printf("Employee %d: %d\n", currentEmployee, total[currentEmployee]);
    }

    return 0;
}

/*Output:
Employee and their total hours in decreasing order:
Employee 7: 41
Employee 6: 37
Employee 0: 34
Employee 4: 32
Employee 3: 31
Employee 1: 28
Employee 5: 28
Employee 2: 20
*/