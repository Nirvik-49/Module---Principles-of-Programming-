/* read values from input file
Practical 4 -  Two-dimensional arrays, Part 2
@Nirvik K.C. */

#include <stdio.h>
#include <stdbool.h>

int main()
{
    int size = 10;  // number of chromosomes
    int sizeR = 3;  // number of criminals
    int sizeC = 10; // number of chromosomes per criminal

    float suspect[size];           // declaring suspect array
    float criminals[sizeR][sizeC]; // declaring criminals two-dimensional array

    // read 10 input values into suspect array from keyboard
    printf("Enter the 10 chromosomes of the suspect seperated by spaces: \n");
    for (int i = 0; i < size; i++)
    {
        scanf("%f", &suspect[i]);
    }
    // read 3 criminals' profiles
    for (int i = 0; i < sizeR; i++)
    {
        printf("Enter the 10 chromosomes of the %dth criminal:\n", i + 1);
        for (int j = 0; j < sizeC; j++)
        {
            scanf("%f", &criminals[i][j]);
        }
    }

    // match suspect profile with each criminal profile
    for (int i = 0; i < sizeR; i++)
    {
        bool match = true;

        for (int j = 0; j < sizeC; j++)
        {
            if (suspect[j] != criminals[i][j])
            {
                match = false;
            }
        }

        // display matching result
        if (match)
        {
            printf("The suspect matches criminal %d.\n", i + 1);
        }
        else
        {
            printf("The suspect does not match criminal %d.\n", i + 1);
        }
    }
    return 0;
}

/*Output:
Enter the 10 chromosomes of the suspect seperated by spaces:
2.3 3.3 4.5 6.7 7.8 2.1 3.2 4.3 5.2 6.5
Enter the 10 chromosomes of the 1th criminal:
2.3 3.3 4.5 6.7 7.8 2.1 3.2 4.3 5.2 6.5
Enter the 10 chromosomes of the 2th criminal:
1.3 0.3 9.5 8.7 5.8 4.1 3.2 2.3 6.2 6.9
Enter the 10 chromosomes of the 3th criminal:
6.3 9.3 4.3 6.4 7.5 2.9 3.0 4.1 5.3 6.5
The suspect matches criminal 1.
The suspect does not match criminal 2.
The suspect does not match criminal 3.
*/