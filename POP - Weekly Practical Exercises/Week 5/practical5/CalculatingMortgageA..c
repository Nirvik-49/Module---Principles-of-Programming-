/* read values from input file
Practical 5 -  Part 1 (a), Functions
@Nirvik K.C. */

#include <stdio.h>
// Function prototypes
double getLarger(double a, double b);
double getSmaller(double a, double b);

int main()
{
    double salary1, salary2;
    double largerSalary, smallerSalary;
    double mortgage;

    // Read in two salaries, salary1, salary2
    printf("Enter two salaries: ");
    scanf("%lf %lf", &salary1, &salary2);

    // Get larger and smaller salaries
    largerSalary = getLarger(salary1, salary2);
    smallerSalary = getSmaller(salary1, salary2);

    // Calculate mortgage
    mortgage = largerSalary * 3;
    mortgage = mortgage + smallerSalary;

    // Display the mortgage
    printf("The maximum size of mortgage is: £%.2f\n", mortgage);

    return 0;
}

// Return the larger salary, largerSalary
double getLarger(double a, double b)
{
    if (a > b)
    {
        return a;
    }
    else
    {
        return b;
    }
}

double getSmaller(double a, double b)
{
    if (a < b)
    {
        return a;
    }
    else
    {
        return b;
    }
}

/*Output:
Enter two salaries: 45000 35000
The maximum size of mortgage is: £170000.00

Enter two salaries: 35000 50000
The maximum size of mortgage is: £185000.00
*/
