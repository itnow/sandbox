#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <cs50.h>

void encrypt(string text, string key, int key_size);

int main(int argc, string argv[])
{
    string key;
    int key_size;
    // Get the key
    if ((argc == 2) && (argv[1] != NULL))
    {
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            if (!isalpha(argv[1][i]))
            {
                printf("Bad input***!\n");
                return 1;
            }
        }
        key = argv[1];
        key_size = strlen(key);
    }
    else
    {
        printf("Bad input!\n");
        return 1;
    }
    
    // Prompt for a text
    string text;
    text = GetString();
    
    // Output encrypted text
    encrypt(text, key, key_size);
    
    return 0;
}


void encrypt(string text, string key, int key_size)
{ 
    int char_idx = 0;
    // Encrypt input
    for (int i = 0; i < strlen(text); i++)
    {
        char encrypted = text[i];
        // Check each char of source text is alpha
        if (isalpha(encrypted))
        {
            char_idx++;
            // Calculate current shift
            int k_idx = (char_idx - 1) % key_size;
            int shift;
            // Check lower
            if (islower(key[k_idx]))
            {
                shift = key[k_idx] - 97;
            }
            // Check upper
            if (isupper(key[k_idx]))
            {
                shift = key[k_idx] - 65;
            }
            
            
            // Check lower
            if (islower(encrypted))
            {
                encrypted = encrypted - 97;
                encrypted = (encrypted + shift) % 26;
                encrypted = encrypted + 97;
            }
            // Check upper
            if (isupper(encrypted))
            {
                encrypted = encrypted - 65;
                encrypted = (encrypted + shift) % 26;
                encrypted = encrypted + 65;
            }
        }
        printf("%c", encrypted);
    }
    printf("\n");
}
