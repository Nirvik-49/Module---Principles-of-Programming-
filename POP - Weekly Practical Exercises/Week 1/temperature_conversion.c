/* Conversion from Celsius to Fahrenheit
Practical 1, Part 3 (b)
Nirvik K.C. */

/* Write a program that reads a Celsius degree in a double
value from the console, then converts it to Fahrenheit and displays the result.
The formula for the conversion is as follows: fahrenheit = (9 / 5) * celsius + 32. */
#include <stdio.h>
int main()
{
    double celsius;
    double fahrenheit;
    // To take input - temperature in Celsius from the user
    printf("\nEnter a degree in Celsius: ");
    scanf("%lf", &celsius);

    // Convert Celsius to Fahrenheit using the given formula
    fahrenheit = (9.0 / 5) * celsius + 32.0;
    printf("\n%.0lf degrees Celsius is %1.lf Fahrenheit.\n", celsius, fahrenheit);
    return 0;
}

/* Output:
Enter a degree in Celsius: 50

50 degrees Celsius is 122 Fahrenheit.
 */