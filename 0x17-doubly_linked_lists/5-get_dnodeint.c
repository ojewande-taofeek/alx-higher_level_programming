#include "lists.h"
/**
 * get_dnodeint_at_index - function that returns
 *                         the nth node of a dlistint_t linked list
 * @head: The pointer to the doubly linked list
 * @index: the index of the node, starting from 0
 * Return: Node at index or NULL if node does not exist
 */

dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *current;
	unsigned int n = 0;

	if (head)
	{
		current = head;
		while (current)
		{
			if (n == index)
				return (current);
			current = current->next;
			n++;
		}
	}
	return (NULL);
}
