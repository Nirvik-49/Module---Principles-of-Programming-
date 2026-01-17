/* read values from input file
Practical 4 - More Programming exercises, Part 4 - 4.1 (Print distinct numbers)
@Nirvik K.C. */

#include <stdio.h>
int main()
{
    int numbers[10]; // declaring an array to hold 10 numbers
    int count = 0;
    int num;
    int i, j;

    printf("Enter ten numbers: ");
    for (i = 0; i < 10; i++)
    {
        scanf("%d", &num);

        // Check if already exists
        for (j = 0; j < count; j++)
        {
            if (numbers[j] == num)
            {
                break;
            }
        }

        // If the number wasn't found in the list, add the new number
        if (j == count)
        {
            numbers[count] = num;
            count++;
        }
    }

    printf("The number of distinct numbers is: %d\n", count);
    printf("The distinct numbers are: ");

    for (i = 0; i < count; i++)
    {
        printf("%d", numbers[i]);

        if (i < count - 1)
        {
            printf(" ");
        }
    }
    printf("\n");

    return 0;
}

/*Output:
Enter ten numbers: 1 2 3 2 1 6 3 4 5 2
The number of distinct numbers is: 6
The distinct numbers are: 1 2 3 6 4 5

Enter ten numbers: 4 1 4 9 1 4 2 9 4 1
The number of distinct numbers is: 4
The distinct numbers are: 4 1 9 2
*/