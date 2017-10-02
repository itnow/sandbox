#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define DATA_SIZE 1000

int ticks = 0;

int bsearch_rec(int key, int data[], int min, int max);
int bsearch_iter(int key, int data[], int size);

int main(void)
{
    // Generate sorted list
    int data[] = {[0] = 1, [DATA_SIZE - 1] = DATA_SIZE};
    for (int i = 0; i < DATA_SIZE; i++)
    {
        data[i] = i + 1;
    }

    // Get data list size
    int size = sizeof(data) / sizeof(int);
    int min = 0;
    int max = size - 1;
    
    // Keys to search for
    int keys[] = {1,  DATA_SIZE / 3, DATA_SIZE / 2, DATA_SIZE, 0};
    for (int i = 0, l = (sizeof(keys) / sizeof(int)); i < l; i++)
    {
        printf("--------------\n");
        
        ticks = 0;
        int key = keys[i];
        printf("iter search for '%i': %i (%i ticks)\n",
            key, bsearch_iter(key, data, size), ticks);
            
        ticks = 0;
        printf("recursion search for '%i': %i (%i ticks)\n",
            key, bsearch_rec(key, data, min, max), ticks);
    }

    return 0;
}


// Returns index of key in array if found, else -1
int bsearch_rec(int key, int data[], int min, int max)
{
    if (min > max)
    {
        return -1;
    }
    else
    {
        ticks++;
        int idx = (min + max) / 2;
        if (key > data[idx])
        {
            return bsearch_rec(key, data, idx + 1, max);
        }
        else if (key < data[idx])
        {
            return bsearch_rec(key, data, min, idx - 1);
        }
        else
        {
            return idx;
        }
    }
}


// Returns index of key in array if found, else -1
int bsearch_iter(int key, int data[], int size)
{
    // Set values for the top and the bottom of the search
    int lower = 0;
    int upper = size - 1;

    // Binary search
    while (lower <= upper)
    {
        ticks++;
        int middle = (upper + lower) / 2;

        if (key == data[middle])
        {
            return middle;
        }
        else if (key > data[middle]) 
        {
            lower = middle + 1;
        }
        else if (key < data[middle])
        {
            upper = middle - 1;
        }
    }
    return -1;
}

