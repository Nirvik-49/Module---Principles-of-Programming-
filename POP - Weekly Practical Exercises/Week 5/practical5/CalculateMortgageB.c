/* read values from input file
Practical 5 -  Part 1 (b)
@Nirvik K.C. */

#include <stdio.h>

// Function declarations (prototypes)
double largerSalary(double salary1, double salary2);
double smallerSalary(double salary1, double salary2);

int main()
{
    // Read in two salaries, salary1, salary2
    double salary1, salary2, mortgage;
    printf("Enter two salaries separated by a space: \n");
    scanf(" %lf %lf", &salary1, &salary2);

    // Calculate mortgage
    mortgage = largerSalary(salary1, salary2) * 3;
    mortgage = mortgage + smallerSalary(salary1, salary2);

    printf("The maximum size of mortgage is: £%.2lf\n", mortgage);

    return 0;
}

// function stub for largerSalary(double, double)
double largerSalary(double salary1, double salary2)
{
    return 1; // function stub
}
// function stub for smallerSalary(double, double)
double smallerSalary(double salary1, double salary2)
{
    return 1; // function stub
}
