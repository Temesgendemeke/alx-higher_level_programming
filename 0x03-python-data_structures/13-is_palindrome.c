#include "lists.h"
#include <stdio.h>

int is_palindrome(listint_t **head)
{
    int count = 0;
    listint_t *current = *head;
    while (current != NULL)
     {
        count++;
        current = current->next;
    }
    printf("%d", count);

    for(int i = 0; i < count/2; i++)
    {
        if (current->n == current->next->n)
        {
            return 0;
        }
        else
        {
            return 1;
        }
        current = current->next;
    }

    
}