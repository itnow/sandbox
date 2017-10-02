#include <stdio.h>

int main(void) {
    int x = 0;
    char c;
    char s[20];
    

    printf("\nNumber please: ");
    scanf("%i", &x);
    
    printf("\nChar please: ");
    // skip to first not null char
    scanf(" %c", &c);
    
    printf("\nString please: ");
    scanf("%s", s);

  
    printf("\nThanks for the %i\n", x);
    printf("Thanks for the %c\n", c);
    printf("Thanks for the %s\n", s);
    
    return 0;
}