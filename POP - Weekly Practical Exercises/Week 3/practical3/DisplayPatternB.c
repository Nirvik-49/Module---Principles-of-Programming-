/* read values from input file
Practical 3, Part 4 - 3.1, Display Pattern B
@Nirvik K.C. */

#include <stdio.h>
int main()
{
    int i, j, rows;
    // Prints number of lines (rows of numbers)
    printf("\nEnter the number of rows: ");
    scanf("%d", &rows);
    for (i = rows; i >= 1; i--) // for number of rows
    {
        for (j = 1; j <= i; j++) // for printing numbers in from 1 to current row value (i)
        {
            printf("%d ", j);
        }
        printf("\n"); // go to next line after printing each row
    }
    return 0;
}
/* Output:
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
*/