#include <stdio.h>

int main(void) {

    int val[] = {1, 2, 3, 4};
    int val2[10];
    char name[] = {'f', 'r', 'e', 'd'};
    int megoray[] = {[0] = 1, [50] = 10, [999] = 321};

    megoray[1201] = 5553;
    val2[15] = 123;

    printf("%i\n", megoray[1201]);
    printf("%i\n", val2[15]);

    int vals_2[2][2] = {{0,1}, {1,0}};
    int vals_3[2][2] = {0,1,1,0};

    return(0);
}