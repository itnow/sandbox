#include <stdio.h>
#include <string.h>

// Variables can be declared in the struct declaration
struct location {
    char* description;
    float latitude;
    float longitude;
}   home_loc = {"GVSU", 42.9709, -85.8857},
    cur_loc = {"Meijer", 42.9901, -85.7222};

struct location get_loc(char* req) {
    struct location loc;
    if(!strcmp(req, "home")) {
        loc = home_loc;
    } else {
        loc = cur_loc;
    }
    return loc;
}

int main(void) {
    struct location my_loc;
    
    my_loc = get_loc("someloc");
    printf("'%s' at %f, %f\n",
        my_loc.description,
        my_loc.latitude,
        my_loc.longitude);

    my_loc = get_loc("home");
    printf("'%s' at %f, %f\n",
        my_loc.description,
        my_loc.latitude,
        my_loc.longitude);

    return 0;
}