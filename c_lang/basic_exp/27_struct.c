#include <stdio.h>

struct location {
    char* description;
    float latitude;
    float longitude;
};

// An array of 3 loc structs is declared
struct location checkins[3] = {
    {"Some loc #1", 11, 11},
    {"Some loc #2", 123, 123},
    {"Some loc #3", 7, 7},
};

int main(void) {
    int i;
    for(i=0; i<3; i++) {
        printf("%s\n", checkins[i].description);    
    }
    return 0;
}