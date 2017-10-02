#include <stdio.h>

int ticks = 0;

void sort(int data[], int start, int end);
void merge(int data[], int l_start, int l_end, int r_start, int r_end);
void print_array(int data[], int size);

int main(void)
{
    int data[] = {44,43,29,28,5,4,23,24,25,2,46,10,11,14,35,36,37,1,38,19,20,21,
                  22,6,7,8,9,42,26,27,30,31,12,13,32,33,34,2,47,1,39,40,15,16,
                  17,18,8,3,2,1};
    int size = sizeof(data) / sizeof(int);
    int start = 0;
    int end = size;
    
    print_array(data, size);
    ticks = 0;

    sort(data, start, end);

    print_array(data, size);
    printf("Size: %i, Ticks %i\n\n", size, ticks);
}

void sort(int data[], int start, int end)
{
    if (end > start)
    {
        int middle = (start + end) / 2;
        sort(data, start, middle);
        sort(data, middle + 1, end);
        merge(data, start, middle, middle + 1, end);
        
    }
}

void merge(int data[], int l_start, int l_end, int r_start, int r_end)
{
    
}

void print_array(int data[], int size)
{
    printf("[");
    for (int i = 0; i < size; i++)
    {
        printf("%i,", data[i]);
    }
    printf("]\n");
}




