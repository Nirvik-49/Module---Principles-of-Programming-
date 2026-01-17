/* read values from input file
Practical 3, Part 4 - 3.1, Display Pattern D
@Nirvik K.C. */

#include <stdio.h>
int main()
{
    int rows;
    printf("Enter the number of rows: ");
    scanf("%d", &rows);
    for (int i = rows; i >= 1; i--) // for number of rows
    {

        for (int j = 1; j <= (rows - i); j++) // calculating spaces
        {
            printf("  "); // printing two spaces
        }
        // Print descending numbers from i to 1
        for (int k = 1; k <= i; k++)
        {
            printf("%d ", k);
        }

        printf("\n"); // go to next line after printing each row
    }
    return 0;
}