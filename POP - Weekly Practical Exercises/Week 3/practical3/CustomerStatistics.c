/* read values from input file
Practical 3, Part 3
@Nirvik K.C. */

#include <stdio.h>
int main()
{
    FILE *fp;
    int total_customers, customer_num, previous_read, current_read;
    int units_used;

    int heavy_users = 0;
    int regular_users = 0;
    int light_users = 0;

    fp = fopen("testInput.txt", "r");

    if (fp == NULL)
    {
        printf("Error opening the file");
        return 1;
    }
    fscanf(fp, "%d", &total_customers);

    int i;
    for (i = 0; i < total_customers; i++)
    {
        fscanf(fp, "%d %d %d", &customer_num, &previous_read, &current_read);

        units_used = current_read - previous_read;

        if (units_used > 1000)
        {
            heavy_users++;
        }
        else if (units_used >= 500)
        {
            regular_users++;
        }
        else if (units_used < 500)
        {
            light_users++;
        }
        else
        {
            printf("Meter reading error for customer %d\n", customer_num);
        }
    }
    printf("Customer Electricity Usage Statistics:\n");
    printf("Heavy users: %d\n", heavy_users);
    printf("Regular users: %d\n", regular_users);
    printf("Light users: %d\n", light_users);
    fclose(fp);
    return 0;
}
/* Output:
Customer Electricity Usage Statistics:
Heavy users: 1
Regular users: 2
Light users: 2
*/