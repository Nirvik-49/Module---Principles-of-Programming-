/* read values from input file
Practical 5 -  Part 1 (c), changes in program  Part 1 (b)
@Nirvik K.C. */

#include <stdio.h>

// Function prototypes declarations
double largerSalary(double salary1, double salary2);
double smallerSalary(double salary1, double salary2);

int main()
{
    double salary1, salary2, mortgage;

    // Read in two salaries from the user, salary1, salary2
    printf("Enter two salaries separated by a space: \n");
    scanf(" %lf %lf", &salary1, &salary2);

    // Calculate mortgage
    mortgage = largerSalary(salary1, salary2) * 3;
    mortgage = mortgage + smallerSalary(salary1, salary2);

    printf("The maximum size of mortgage is: £%.2lf\n", mortgage);
    return 0;
}

// Replace the function stubs
// Function for selecting larger salary
double largerSalary(double salary1, double salary2)
{
    if (salary1 > salary2)
    {
        return salary1;
    }
    else
    {
        return salary2;
    }
} // largeSalary

// Function for selecting smaller salary
double smallerSalary(double salary1, double salary2)
{
    if (salary1 > salary2)
    {
        return salary2;
    }
    else
    {
        return salary1;
    }
} // smallerSalary

/*Output:
Enter two salaries separated by a space:
65000 45000
The maximum size of mortgage is: £240000.00
*/