#include <stdio.h>
#include <stdlib.h>

struct node
{
    struct node *prev;
    int data;
    struct node *next;
};
int main()
{
    struct node *head = malloc(sizeof(struct node));
    head->prev = NULL;   //first  linked list.
    head->data = 1;      //the data being inputed.
    head->next = NULL;   // the header pointer to point NULL.

    return 0;
}