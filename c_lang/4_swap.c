#include <stdio.h>


void swap(int x, int y)
{
    int tmp = x;
    x = y;
    y = tmp;
}

int main(void)
{
   int x = 1;
   int y = 5;
   printf("%d, %d\n", x, y);
   swap(x, y);
   printf("%d, %d\n", x, y);
}
