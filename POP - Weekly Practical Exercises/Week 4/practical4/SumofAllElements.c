/* read values from input file
Practical 4 - More Programming exercises, Part 4 - 4.3 (Sum elements column by column)
@Nirvik K.C. */

#include <stdio.h>
int main()
{
    double matrix[3][4]; // 3 rows and 4 columns
    int row, col;
    double sum; // sum of elements in each column

    printf("Enter a 3-by4 matrix row by row:\n");

    // Read the matrix elements from user input
    for (row = 0; row < 3; row++)
    {
        for (col = 0; col < 4; col++)
        {
            scanf("%lf", &matrix[row][col]);
        }
    }

    // Calculate and display the sum of each column
    for (col = 0; col < 4; col++)
    {
        sum = 0.0;
        // Sum of all elements in the current column
        for (row = 0; row < 3; row++)
        {
            sum += matrix[row][col];
        }
        printf("Sum of the elements at column %d is %.1f\n", col, sum);
    }
    return 0;
}

/*Output:
Enter a 3-by-4 matrix row by row:
1.5 2 3 4
5.5 6 7 8
9.5 1 3 1
Sum of the elements at column 0 is 16.5
Sum of the elements at column 1 is 9.0
Sum of the elements at column 2 is 13.0
Sum of the elements at column 3 is 13.0

Enter a 3-by4 matrix row by row:
1.2 0.5 4.0 2.1
3.0 1.5 2.0 0.0
5.5 2.5 1.0 3.6
Sum of the elements at column 0 is 9.7
Sum of the elements at column 1 is 4.5
Sum of the elements at column 2 is 7.0
Sum of the elements at column 3 is 5.7
*/