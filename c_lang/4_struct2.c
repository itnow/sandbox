#include <cs50.h>
#include <stdio.h>
#include <string.h>

#include "structs.h"

#define STUDENTS 3

int main(void)
{
    student students[STUDENTS];
    
    for (int i = 0; i < STUDENTS; i++)
    {
        printf("Student's name: \n");
        students[i].name = GetString();
        
        printf("Student's house: \n");
        students[i].house = GetString();
    }
    
    for (int i = 0; i < STUDENTS; i++)
    {
        printf("%s is in %s\n", students[i].name, students[i].house);
    }
    
    // Free memory?
    for (int i = 0; i < STUDENTS; i++)
    {
        free(students[i].name);
        free(students[i].house);
    }

    return 0;
}