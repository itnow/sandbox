#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <cs50.h>

int main(void)
{
    printf("Say something: ");
    string s = GetString();
    if (s == NULL)
    {
        return 1;
    }

    char* t = malloc((strlen(s) + 1) * sizeof(char));
    if (t == NULL)
    {
        free(s);
        return 1;
    }

    for (int i = 0, l = strlen(s); i <= l; i++)
    {
        //t[i] = s[i];
        *(t + i) = *(s + i);
    }
    
    if (strlen(t) > 0)
    {
        //t[0] = toupper(t[0]);
        *t = toupper(*t);
        *(t + 1) = toupper(*(t + 1));
    }
    
    printf("\n%s <-> %s\n", s, t);
    
    return 0;
}