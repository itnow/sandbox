#include <stdio.h>

int factorial(int n) {
    int retval = 1;
    if(n != 1) {
        retval = n * factorial(n-1);
    }
    return retval;
}

int main(void) {
    printf("%d! = %d\n", 7, factorial(7));
}
