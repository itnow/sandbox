#include <stdio.h>

int main(void)
{
    int x = 10;
    int* ptr = &x;
    int y = *ptr;
    *ptr = 20;
  
    printf("x: %d\n", x);
    printf("ptr: %d\n", *ptr);
    printf("y: %d\n", y);
}