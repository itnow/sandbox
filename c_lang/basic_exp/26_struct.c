#include <stdio.h>

// Structs within structs
struct geofix {
    float latitude;
    float longitude;
};

struct location {
    char* description;
    // nested structs
    struct geofix pos;
}   home_loc = {"GVSU", {42.9709, -85.8857}};

void print_loc(struct location some_loc) {
    printf("My curr location is '%s' geo: %f, %f\n",
        // References to struct members must mirror the nesting hierarchy.
        some_loc.description,
        some_loc.pos.latitude,
        some_loc.pos.longitude);
}

int main(void) {
    print_loc(home_loc);
    return 0;
}