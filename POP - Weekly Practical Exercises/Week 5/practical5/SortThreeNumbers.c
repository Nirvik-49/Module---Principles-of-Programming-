/* read values from input file
Practical 5 -  Part 3, 5.1 (Sort three numbers)
@Nirvik K.C. */

#include <stdio.h>
void DisplaySortedNumbers(double num1, double num2, double num3)
{
    double smallestNum, middleNum, largestNum;

    // Determine the smallest number
    if (num1 <= num2 && num1 <= num3)
    {
        smallestNum = num1;
    }
    else if (num2 <= num1 && num2 <= num3)
    {
        smallestNum = num2;
    }
    else
    {
        smallestNum = num3;
    }

    // Determine the largest number
    if (num1 >= num2 && num1 >= num3)
    {
        largestNum = num1;
    }
    else if (num2 >= num1 && num2 >= num3)
    {
        largestNum = num2;
    }
    else
    {
        largestNum = num3;
    }

    // Determine the number middle number (neither smallest nor largest)
    if (num1 != smallestNum && num1 != largestNum)
    {
        middleNum = num1;
    }
    else if (num2 != smallestNum && num2 != largestNum)
    {
        middleNum = num2;
    }
    else
    {
        middleNum = num3;
    }

    // Display the three numbers in increasing order
    printf("%.2lf, %.2lf, %.2lf\n", smallestNum, middleNum, largestNum);
}

int main()
{
    double a, b, c;

    printf("Enter the three numbers: ");
    scanf(" %lf %lf %lf", &a, &b, &c);

    printf("The numbers in increasing order are: ");
    DisplaySortedNumbers(a, b, c);

    return 0;
}

/*Output:
Enter the three numbers: 100 75 35
The numbers in increasing order are: 35.00, 75.00, 100.00

Enter the three numbers: 7.5 2.3 4.0
The numbers in increasing order are: 2.30, 4.00, 7.50
*/