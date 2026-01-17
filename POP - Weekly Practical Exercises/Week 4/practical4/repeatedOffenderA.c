/* read values from input file
Practical 4 -   Arrays (exercise) , Part 3
@Nirvik K.C. */

#include <stdio.h>
#include <stdbool.h>

int main()
{
    FILE *fp;
    float suspect[10];
    float criminals[5][10];
    int numCriminals;
    int i, j;
    int match;
    int foundAnyMatch = 0;

    // Open the input file
    fp = fopen("dna_input.txt", "r");
    if (fp == NULL)
    {
        printf("Error opening the file!\n");
        return 1;
    }

    // Read suspect profile
    for (i = 0; i < 10; i++)
    {
        fscanf(fp, "%f", &suspect[i]);
    }

    // Read the number of criminals
    fscanf(fp, "%d", &numCriminals);

    // Read the profiles of the criminals

    for (i = 0; i < numCriminals; i++)
    {
        for (j = 0; j < 10; j++)
        {
            fscanf(fp, "%f", &criminals[i][j]);
        }
    }

    fclose(fp);

    printf("DNA Matching Report\n");
    foundAnyMatch = 0;

    for (int i = 0; i < numCriminals; i++)
    {
        match = 1;

        for (j = 0; j < 10; j++)
        {
            if (suspect[j] != criminals[i][j])
            {
                match = 0;
                break;
            }
        }

        if (match)
        {
            printf("Suspect matches with Criminal %d\n", i);
            foundAnyMatch = 1;
        }
        else
        {
            printf("Suspect does not match with Criminal %d\n", i);
        }
    }

    printf("\n");
    if (foundAnyMatch)
    {
        printf("The suspect is a repeated offender.\n");
    }
    else
    {
        printf("The suspect is not a repeated offender.\n");
    }
    return 0;
}

/*Output:
DNA Matching Report
Suspect matches with Criminal 0
Suspect does not match with Criminal 1
Suspect does not match with Criminal 2
Suspect does not match with Criminal 3
Suspect does not match with Criminal 4

The suspect is a repeated offender.
*/