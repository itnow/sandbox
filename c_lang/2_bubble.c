#include <stdio.h>

int ticks = 0;

void bubble(int data[], int size);
void print_array(int data[], int size);

int main(void)
{
    int data[] = {44,43,29,28,5,4,23,24,25,2,46,10,11,14,35,36,37,1,38,19,20,21,
                  22,6,7,8,9,42,26,27,30,31,12,13,32,33,34,2,47,1,39,40,15,16,
                  17,18,3,2,1,8};
    int size = sizeof(data) / sizeof(int);

    print_array(data, size);
    ticks = 0;
    bubble(data, size);
    printf("Size: %i, Ticks %i\n\n", size, ticks);

    return 0;
}


void bubble(int data[], int size)
{
    for (int k = 0; k < size - 1; k++)
    {
        ticks++;
        int swaps = 0;
        int tmp = 0;

        for (int i = 0; i < size - 1 - k; i++)
        {
            ticks++;
            if (data[i] > data[i + 1])
            {
                tmp = data[i];
                data[i] = data[i + 1];
                data[i + 1] = tmp;
                swaps++;
            }
        }
        if (!swaps)
        {
            break;
        }
    }
    print_array(data, size);
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

