/* read values from input file
Practical 3, Part 1 (a)
@Nirvik K.C. */

#include <stdio.h>
FILE *fp; // define a file pointer for the file to hold a disk location
int main()
{
    // open the file and assign its address/disk location to file pointer
    fp = fopen("inputFile.txt", "r"); // relative pathname used
    // declare variables for holding the values of input
    char firstWord[20]; // a word/string up to 20 characters
    char secondWord[20];
    int num;
    printf("Reads two words and an integer from file \n");
    // Read two words and an integer from file
    // fscanf instead of scanf used, and file pointer needed
    fscanf(fp, "%s %s %d", firstWord, secondWord, &num);
    // display two words and an integer
    printf("Displays back what has been read from input file:\n");
    printf("%s %s \n%d \n", firstWord, secondWord, num);
    fclose(fp); // Closes the file
    return 0;
}

/* Output :
Reads two words and an integer from file
Displays back what has been read from input file:
Hello World
4
*/
