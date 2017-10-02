#include <stdio.h>
#include <string.h>

struct location {
    char* description;
    float latitude;
    float longitude;
};

void foo(struct location check_loc) {
    if((check_loc.description != NULL) && !strcmp(check_loc.description, "Known location name")) {
        printf("You are in '%s'\n", check_loc.description);
    } else {
        printf("You somwere we don't know yet!\n");
    }
}

int main(void) {
    struct location some_loc = {"Known location name", 42.9709, -85.8857};
    foo(some_loc);
    return 0;
}