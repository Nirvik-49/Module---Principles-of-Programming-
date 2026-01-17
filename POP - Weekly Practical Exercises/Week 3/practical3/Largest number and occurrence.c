/* read values from input file
Practical 3, Part 4 - 3.2  (Occurrence of max numbers)
@Nirvik K.C. */
#include <stdio.h>
int main()
{
    int num;
    int number;
    int max;
    int count = 0;
    printf("Enter numbers (type 0 to stop):\n");
    // Read the first number

    scanf("%d", &number);
    while (number != 0)
    {
        if (number > max)
        {
            max = number;
            count = 1; // starting a new count
        }
        else if (number == max)
        {
            count++;
        }
        scanf("%d", &number); // Read the next number
    }
    // Display the maximum number and its occurrence after 0 is entered at last
    if (max == 0)
    {
        printf("No numbers were entered.\n");
    }
    else
    {
        printf("The largest number is %d.\n", max);
        printf("The occurrence of the largest number is %d times.\n", max, count);
    }
    return 0;
}

/* Output:
Enter numbers (type 0 to stop):
3 5 2 5 5 5 0
The largest number is 5.
The occurrence of the largest number is 5 times.*/