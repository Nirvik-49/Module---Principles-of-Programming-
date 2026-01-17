/* read values from input file
Practical 3, Part 4 - 3.1, Display Pattern C
@Nirvik K.C. */

#include <stdio.h>
int main()
{
    int rows;
    int i, j, k;
    printf("Enter the number of rows: ");
    scanf("%d", &rows);

    for (int i = 1; i <= rows; i++)
    {
        for (int j = 1; j <= (rows - i); j++) // calculating spaces
        {
            printf("  "); // printing two spaces
        }

        // Print descending numbers from i to 1
        for (int k = i; k >= 1; k--)
        {
            printf("%d ", k);
        }

        printf("\n"); // go to next line after printing each row
    }

    return 0;
}

/*Output:
Enter the number of rows: 6
          1
        2 1
      3 2 1
    4 3 2 1
  5 4 3 2 1
6 5 4 3 2 1
*/