#include "lists.h"

/**
 * free_dlistint - function that frees a dlistint_t list.
 * @head: Pointer to the doubly linked list head
 * Return: Nothing
 */

void free_dlistint(dlistint_t *head)
{
	dlistint_t *current;

	if (head)
	{
		while (head)
		{
			current = head;
			head = current->next;
			free(current);
		}

	}
}
