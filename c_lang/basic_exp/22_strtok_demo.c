#include <string.h>
#include <stdio.h>

int main(int argc, char* argv[]) {
    int line_cnt = 0;
    FILE *fp = fopen("data_text_input.txt", "r");
    char buf[1024];

    printf("Loading file...\n");

    char* ptr;
    while((ptr = fgets(buf, 1024, fp)) != NULL) {
        buf[strlen(buf)] = 0;
        line_cnt++;
        char* tok;
        tok = strtok(buf, " .!\t\n");
        while(tok != NULL){
            printf("[%s] ", tok);
            tok = strtok(NULL, " .!\t\n");
        }
    }
    printf("\nDone... %d lines read.\n", line_cnt);
}