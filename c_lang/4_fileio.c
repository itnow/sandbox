#include <stdio.h>

int main(void)
{
    FILE* fp = fopen("somefile.txt", "w");
    if (fp == NULL)
    {
        return 1;
    }
    fprintf(fp, "Hello!");
    fclose(fp);
}