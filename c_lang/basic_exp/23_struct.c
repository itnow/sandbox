#include <stdio.h>

// Type definition, global.
// Don't allocate memory here, just describe new type. 
struct location {
    char* description;
    float latitude;
    float longitude;
};

int main(void) {
    // Declaration of a variable of type struct.
    // Memory allocated here to hold values of this particular structure.
    struct location some_my_loc = {"Some location name", 42.9709, -85.8857};

    printf("Come visit '%s' at geo: %f, %f\n",
        some_my_loc.description,
        some_my_loc.latitude,
        some_my_loc.longitude);
}