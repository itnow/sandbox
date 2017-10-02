#include <stdio.h>

int main(void) {
    int i=2, j=3, m=7, r1, r2;

    r1 = ++i + j; 
    r2 = m-- + j;

    printf("pre-incremented res: %d (i=%d)\n", r1, i);
    printf("post-decremented res: %d (m=%d)\n", r2, m);

    return(0);
}