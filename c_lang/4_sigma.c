#include <stdio.h>

int sigma(int num);
int main(void)
{
   int res = sigma(50);
   printf("%d\n", res);
}
int sigma(int num)
{
    if (num <= 0)
        return 0;
    else
        return num + sigma(num-1);
}