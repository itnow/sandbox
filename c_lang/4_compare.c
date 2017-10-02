#include <stdio.h>
#include <string.h>

int main(void)
{
    printf("Say something: ");
    char* s = GetString();
    
    printf("Say something: ");
    char* t = GetString();
    
    if (s != NULL && t != NULL)
    {
        if (strcmp(s, t) == 0)
        {
            printf("You type same thing!\n");
        }
        else
        {
            printf("You type different thing!\n");
        }
    }
    
    printf("size %lu\n", sizeof(s));
}