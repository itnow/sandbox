#include <stdio.h>

typedef struct foo {
    int i;
    char a;
    double d;
} Foo;

typedef union bar {
    int i;
    char a;
    double d;
} Bar;

int main(void) {
    Foo wow;
    Bar yay;
    printf("Size of Foo is %lu\n", sizeof(wow));
    printf("Size of Bar is %lu\n", sizeof(yay));
    return 0;
}