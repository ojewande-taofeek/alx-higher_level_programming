#include "lists.h"

/**
 * dlistint_len - function that returns the number of
 *                elements in a linked dlistint_t list.
 * @h: The head pointer of the doibly linked list
 * Return: the number of nodes, n
 */

size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *current;
	size_t n = 0;

	current = h;
	while (current != NULL)
	{
		n++;
		current = current->next;
	}
	return (n);
}
