#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int val;
    struct node* next;
}
node;

node* head = NULL;

void print_last()
{
    // if the list is empty
    if (head == NULL)
    {
        printf("List empty. No last element.\n");
    }
    else
    {
        // traversal pointer
        node* crawler = head;
        
        // until the end of the list
        while (crawler->next != NULL)
        {
            // keep travesing the list
            crawler = crawler->next;
        }
        
        printf("The last int is %d\n", crawler->val);
    }
}

void insert_after_third(int to_insert)
{
    if (head == NULL)
    {
        printf("List empty. No 3rd position exists.\n");
    }
    else
    {
        node* crawler = head;
        for (int i = 1; i < 3; i++)
        {
            if (crawler->next == NULL)
            {
                printf("List short, no 3rd position exists.\n");
            }
            else
            {
                crawler = crawler->next;
            }
        }
        
        // init a new node to go between the two
        node* new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            printf("Out of heap memory!\n");
            return;
        }
        // store the int value
        new_node->val = to_insert;
        // point next to third node's successor
        new_node->next = crawler->next;
        // point previous node at the new one
        crawler->next = new_node;
    }
}