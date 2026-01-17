/* read values from input file
Practical 3, Part 1 (b)
@Nirvik K.C. */

#include <stdio.h>
FILE *fp; // define a file pointer for the file to hold a disk location
int main()
{
    FILE *fp;
    // open file for reading
    fp = fopen("inputFile.txt", "r");
    if (fp == NULL)
    {
        {
            printf("Error opening the file");
            return 1;
        }
    }
    // declare variables for holding the values of input
    char firstWord[20];
    char secondWord[20];
    int num;
    printf("Reads two words and an integer from file \n");
    // Changed the layout of the values in the input file - Hello World 4
    // Read two words and an integer from file
    fscanf(fp, "%s %s %d", firstWord, secondWord, &num);
    // Display two words and an integer
    printf("Displays back what has been read from input file:\n");
    printf("%s %s %d \n \n", firstWord, secondWord, num); // Display the three input values on the same line

    fclose(fp); // Closes the file
    return 0;
}
// Output : Hello World 4