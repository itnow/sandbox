#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <cs50.h>

void encrypt(string text, int key);

int main(int argc, string argv[])
{
    // Get the key
    int key = 0;
    if ((argc == 2) && (argv[1] != NULL))
    {
        key = atoi(argv[1]);
    }
    else
    {
        printf("Bad input!\n");
        return 1;
    }
    
    // Check is key a positive
    if (key < 1)
    {
        return 1;
    }
    else
    {
        key = key % 26;
    }

    // Prompt for a text
    string text;
    text = GetString();
    
    // Output encrypted text
    encrypt(text, key);

    
    return 0;
}


void encrypt(string text, int key)
{ 
    // Encrypt input
    for (int i = 0; i < strlen(text); i++)
    {
        char encrypted = text[i];
        // Check alpha
        if (isalpha(encrypted))
        {
            // Check lower
            if (islower(encrypted))
            {
                encrypted = encrypted - 97;
                encrypted = (encrypted + key) % 26;
                encrypted = encrypted + 97;
            }
            // Check upper
            if (isupper(encrypted))
            {
                encrypted = encrypted - 65;
                encrypted = (encrypted + key) % 26;
                encrypted = encrypted + 65;
            }
        }
        printf("%c", encrypted);
    }
    printf("\n");
}
