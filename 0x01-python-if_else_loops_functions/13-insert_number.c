#include "lists.h"

/**
 * insert_node : function in C that inserts a number into a sorted singly linked list.
 * 
*/

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *current;
    listint_t *newnode;
    newnode = malloc(sizeof(listint_t));
    if (!newnode)
    {
        free(newnode);
        return (NULL);
    }
    newnode->n = number;
    newnode->next = NULL;


    current = *head;
    if(current == NULL || current->n >= number)
    {
        newnode->next = current;
        *head = newnode;
        return *head;
    }
    
    while (current && current->next->n < number)
    {
            current = current->next;
    }
    if (current->n < number) {
        newnode->next = current->next;
        current->next = newnode;
    }
    return (current);
}

