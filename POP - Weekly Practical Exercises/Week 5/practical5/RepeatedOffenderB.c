/* read values from input file
Practical 5 -  Part 2, Using Functions and Pointers
@Nirvik K.C. */

#include <stdio.h>
#include <stdbool.h>

// Function prototype declarations
bool matchingProfiles(float suspect[], float aCriminal[]);

FILE *fp; //  defined a file pointer for the file
int main()
{
    // Open the input file
    fp = fopen("dna_input.txt", "r");
    if (fp == NULL)
    {
        printf("Error: Could not open file dna_input.txt\n");
        return 1;
    }
    int size = 10;
    float suspect[size]; // declaring suspect array
    int sizeR;
    int sizeC = 10;

    // Read 10 input values into suspect array
    printf("Reading the 10 gene chromosomes of the suspect \n");
    for (int i = 0; i < size; i++)
    {
        fscanf(fp, " %f", &suspect[i]);
    }

    // Read the number of criminals
    printf("Reading the number of criminals \n");
    fscanf(fp, " %d", &sizeR);

    float criminals[sizeR][sizeC]; // declaring criminals array

    // read multiple profiles of 10 input values into criminals array
    for (int i = 0; i < sizeR; i++)
    {
        printf("Read the 10 gene chromosomes of %dth criminal \n", i + 1);
        for (int j = 0; j < sizeC; j++)
        {
            fscanf(fp, " %f", &criminals[i][j]);
        }
    }

    // match suspect with each criminal and display the result
    printf("DNA matching report of the suspect with criminals:\n");
    bool foundAnyMatch = false;
    for (int i = 0; i < sizeR; i++)
    {
        if (matchingProfiles(suspect, criminals[i]))
        {
            printf("The %dth criminal matches! \n", i + 1);
            foundAnyMatch = true;
        }
        else
        {
            printf("The %dth criminal doesn't match! \n", i + 1);
        }
    }

    if (foundAnyMatch)
    {
        printf("The suspect is a repeated offender! \n");
    }
    else
    {
        printf("The suspect is not a repeated offender! \n");
    }

    fclose(fp);
    return 0;
}

bool matchingProfiles(float suspect[], float aCriminal[])
{
    for (int i = 0; i < 10; i++)
    {
        if (suspect[i] != aCriminal[i])
        {
            return false; // mismatch found
        }
    }
    return true; // all values matched
}

/*Output:
Reading the 10 gene chromosomes of the suspect
Reading the number of criminals
Read the 10 gene chromosomes of 1th criminal
Read the 10 gene chromosomes of 2th criminal
Read the 10 gene chromosomes of 3th criminal
Read the 10 gene chromosomes of 4th criminal
Read the 10 gene chromosomes of 5th criminal
DNA Matching Report of the Suspect with Criminals
The 1th criminal matches!
The 2th criminal doesn't match!
The 3th criminal doesn't match!
The 4th criminal doesn't match!
The 5th criminal doesn't match!
The suspect is a repeated offender!
*/