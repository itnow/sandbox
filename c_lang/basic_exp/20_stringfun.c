#include <stdio.h>

int main(int argc, char* argv[]) {
    char greeting[6] = {'h', 'e', 'l', 'l', 'o', '\0'};
    char farewell[] = {"bye!"};
    
    char* str1 = greeting;
    char* str2 = &greeting[3];


    printf("%s\n", greeting);
    printf("%s\n", str1);
    printf("%s\n", str2);

    printf("size of greeting: %lu\n", sizeof(greeting));
    printf("size of farewell: %lu\n", sizeof(farewell));

    printf("size of str1: %lu\n", sizeof(str1));
    printf("size of str2: %lu\n", sizeof(str2));

    printf("size of &greeting[3]: %lu\n", sizeof(&greeting[3]));
}