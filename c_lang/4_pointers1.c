#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int* x;
    int* y;
    
    x = malloc(sizeof(int));
    
    *x = 42;
    
    printf("%d\n", *x);
    
    y = x;
    *y = 13;

    printf("%d, %d\n", *x, *y);    
    
    return 0;
}