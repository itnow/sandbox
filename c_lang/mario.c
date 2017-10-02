#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int p_height;
    
    // Promt and validate user input
    do
    {
        printf("height: ");
        p_height = GetInt();
    } while (p_height < 0 || p_height > 23);

    // Draw the half-pyramid
    for (int i = 0; i < p_height; i++)
    {
        for (int j = 0; j < p_height - 1 - i; j++)
        {
            printf(" ");
        }
        for (int j = 0; j <= i + 1; j++)
        {
            printf("#");
        }
        printf("\n");
    }
    return 0;

    // commets blown up for style 50
    //
    //
}
