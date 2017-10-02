#include <string.h>
#include <stdio.h>

int my_strlen(char* str) {
    printf("Pls, standbuy, rocket science is here...\n");
    return strlen(str);
}


int main(int argc, char* argv[]) {
    char* greet = "hello";
    int (*my_ptr)(char*);  // declare

    my_ptr = my_strlen;  // assign

    int i = (*my_ptr)(greet);  // invoke
    printf("%d\n", i );
}