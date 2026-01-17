/* read values from input file
Practical 4 - More Programming exercises, Part 4 - 4.2 (Find the smallest number)
@Nirvik K.C. */

#include <stdio.h>
int main()
{
    double numbers[10]; // declaring an array to store 10 double values
    double min;
    int i;

    printf("Enter ten numbers: ");
    // Read 10 double numbers from the user
    for (int i = 0; i < 10; i++)
    {
        scanf("%lf", &numbers[i]);
    }

    // Find the smallest number
    min = numbers[0];
    for (int i = 0; i < 10; i++)
    {
        if (numbers[i] < min)
        {
            min = numbers[i];
        }
    }

    // Display the smallest number
    printf("The smallest number is: %.1f\n", min);

    return 0;
}

/*Output:
Enter ten numbers: 1.9 2.5 3.7 2 1.5 6 3 4 5 2
The smallest number is: 1.5

Enter ten numbers: 4.8 9.1 2.3 0.0 -5.6 7.2 1.1 3.4 6.9 8.0
The smallest number is: -5.6
*/
