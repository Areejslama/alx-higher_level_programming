#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * reverse_list - Reverses a linked list
 * @head: The head of the linked list
 *
 * Return: The head of the reversed linked list
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL, *current = head, *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: The head of the singly linked list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    if (head == NULL || *head == NULL)
        return (1); 

    listint_t *slow = *head, *fast = *head;
    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    }
    slow = reverse_list(slow);

    while (slow != NULL)
    {
        if ((*head)->n != slow->n)
            return (0);

        *head = (*head)->next;
        slow = slow->next;
    }

    return (1);
}
