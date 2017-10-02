#include <stdio.h>

// Swap the value pointed to by v1 with the value pointed to by v2
void swap(int *v1, int *v2) {
    int tmp;
    tmp = *v1;
    *v1 = *v2;
    *v2 = tmp;
}

int main(void) {
    int i = 2, j = 5;
    printf("i=%d, j=%d\n", i, j);
    swap(&i, &j);
    printf("i=%d, j=%d\n", i, j);
    return 0;
}