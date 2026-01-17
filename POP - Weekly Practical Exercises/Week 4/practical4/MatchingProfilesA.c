/* read values from input file
Practical 4 -  One-dimensional arrays, Part 1
@Nirvik K.C. */

#include <stdio.h>
#include <stdbool.h>

int main()
{
    int size = 10;
    float suspect[size];  // declaring suspect array
    float criminal[size]; // declaring criminal array

    // read 10 input values into suspect array from keyboard
    printf("Enter the 10 chromosomes of the suspect separated by spaces: \n");
    for (int i = 0; i < size; i++)
    {
        scanf(" %f", &suspect[i]);
    }

    // read 10 input values into criminal array from keyboard
    printf("Enter the 10 chromosomes of the criminal separated by spaces: \n");
    for (int i = 0; i < size; i++)
    {
        scanf(" %f", &criminal[i]);
    }

    // match two profiles
    bool match = true;
    for (int i = 0; i < size; i++)
    {
        if (suspect[i] != criminal[i])
        {
            match = false;
        }
    }
    // display matching result
    if (match)
    {
        printf("The two profiles match! \n");
    }
    else
    {
        printf("The two profiles don't match! \n");
    }
    return 0;
}

/* Output:
Test Case 1:
Enter the 10 chromosomes of the suspect separated by spaces:
2.3 3.3 4.5 6.7 7.8 2.1 3.2 4.3 5.2 6.5
Enter the 10 chromosomes of the criminal separated by spaces:
2.3 3.3 4.5 6.7 7.8 2.1 3.2 4.3 5.2 6.5

Test Case 2:
Enter the 10 chromosomes of the suspect separated by spaces:
2.3 3.3 4.5 6.7 7.8 2.1 3.2 4.3 5.2 6.5
Enter the 10 chromosomes of the criminal separated by spaces:
1.3 0.3 9.5 8.7 5.8 4.1 3.2 2.3 6.2 6.9
The two profiles don't match!
*/