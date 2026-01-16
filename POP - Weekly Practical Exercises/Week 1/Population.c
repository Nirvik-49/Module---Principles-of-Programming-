/* Print the total population for next five years
Practical 1, Part 3 (a)
Nirvik K.C. */

/* Write a program to display the population for each of the next five years.
Assume the current population is 312,032,486 and one year has 365 days. */
#include <stdio.h>
int main()
{
    double population = 312032486.0;
    double time = 365 * 24 * 60 * 60;
    float birth = time / 7;      // One birth every 7 seconds
    float death = time / 13;     // One death every 13 seconds
    float immigrant = time / 45; // One new immigrant every 45 seconds

    double net_population = birth - death + immigrant;
    printf("\nYearly Population: \n");

    double population_year1 = population + net_population;
    printf("First year population: %.0lf\n", population_year1);

    double population_year2 = population_year1 + net_population;
    printf("Second year population: %.0lf\n", population_year2);

    double population_year3 = population_year2 + net_population;
    printf("Third year population: %.0lf\n", population_year3);

    double population_year4 = population_year3 + net_population;
    printf("Fourth year population: %.0lf\n", population_year4);

    double population_year5 = population_year4 + net_population;
    printf("Fifth year population: %.0lf\n", population_year5);
    return 0;
}

/* Output :
Yearly Population:
First year population: 314812583
Second year population: 317592680
Third year population: 320372776
Fourth year population: 323152873
Fifth year population: 325932970
 */