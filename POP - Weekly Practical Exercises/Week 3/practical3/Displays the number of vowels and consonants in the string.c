/* read values from input file
Practical 3, Part 4 - 3.3  (Count vowels and consonants)
@Nirvik K.C. */

#include <stdio.h>
#include <string.h>
int main()
{
    char str[100];
    int vowels = 0, consonants = 0;
    int i, j;
    char vowel_list[10] = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'};

    printf("\nEnter a string: ");

    // To read the whole line including spaces
    fscanf(stdin, "%[^\n]", str); // using %[^\n] to read string with spaces
    for (int i = 0; i < strlen(str); i++)
    {
        char ch = str[i];

        // Check if the character is a letter (A-Z or a-z)
        if ((ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z'))
        {
            int isVowel = 0;
            for (int j = 0; j < 10; j++)
            {
                if (ch == vowel_list[j])
                {
                    isVowel = 1;
                    break;
                }
            }
            if (isVowel)
            {
                vowels = vowels + 1;
            }
            else
            {
                consonants = consonants + 1;
            }
        }
    }
    printf("The number of vowels is %d\n", vowels);
    printf("The number of consonants is %d\n", consonants);

    return 0;
}
/* Output:
Enter a string: Programming is fun
The number of vowels is 5
The number of consonants is 11 */