#include <string.h>
#include <stdio.h>

int main(int argc, char* argv[]) {
    char c = 'x';

    char greeting[6] = {'h', 'e', 'l', 'l', 'o', '\0'};
    char farewell[] = {"byebyebyebyebye!"};

    strcpy(farewell, greeting);
    printf("farewell=%s, greeting=%s\n", farewell, greeting);

    char greeting2[6] = {'h', 'e', 'l', 'l', 'o', '\0'};
    char farewell2[] = {"byebyebyebyebye!"};
    
    strncpy(farewell2, greeting2, 5);
    printf("farewell2=%s, greeting2=%s\n", farewell2, greeting2);
}