#include <stdio.h>

void printer(int num);
int main(void)
{
    int num = 5;
    printer(num);
    return 0;
}
void printer(int num)
{
    if (num <=0)
    {
        printf("I'm finished\n");
        return;
    }
    else
    {
        printf("Hello\n");
        printer(num - 1);
    }
}