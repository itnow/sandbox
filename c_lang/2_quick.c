#include <stdio.h>

int ticks = 0;

void quick(int data[], int start, int end);
int partition(int data[], int start, int end);
void print_array(int data[], int size);

int main(void)
{
    int data[] = {44,43,29,28,5,4,23,24,25,2,46,10,11,14,35,36,37,1,38,19,20,21,
                  22,6,7,8,9,42,26,27,30,31,12,13,32,33,34,2,47,1,39,40,15,16,
                  17,18,3,2,1,8};
    int size = sizeof(data) / sizeof(int);
    int start = 0;
    int end = size - 1;
    
    print_array(data, size);
    quick(data, start, end);
    print_array(data, size);
    
    printf("Size: %i, Ticks %i\n\n", size, ticks);
}

void quick(int data[], int start, int end)
{
    if (start < end)
    {
        int part_idx = partition(data, start, end);
        quick(data, start, part_idx - 1);
        quick(data, part_idx + 1, end);
    }
    ticks++;
}

int partition(int data[], int start, int end)
{
    int pivot = data[end];
    int part_idx = start;
    
    for (int i = start; i < end; i++)
    {
        if (data[i] <= pivot)
        {
            int tmp = data[i];
            data[i] = data[part_idx];
            data[part_idx] = tmp;
            part_idx++;
        }
        ticks++;
    }
    
    int tmp = data[part_idx];
    data[part_idx] = data[end];
    data[end] = tmp;
    
    return part_idx;
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