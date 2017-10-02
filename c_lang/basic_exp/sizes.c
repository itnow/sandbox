#include <stdio.h>

int main(void) {
    int i;
    double d;
    char c;

    printf("int: %lu\n", (unsigned long)sizeof(i));
    printf("double: %lu\n", (unsigned long)sizeof(d));
    printf("char: %lu\n", (unsigned long)sizeof(c));
}