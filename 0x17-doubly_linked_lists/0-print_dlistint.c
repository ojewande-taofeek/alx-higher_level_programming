#include "lists.h"
/**
 * print_dlistint - function that prints all the elements of a dlistint_t list.
 * @h: The head pointer to the doubly linked list
 * Return: the number of nodes, n
 */

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *current;
	size_t n = 0;

	current = h;

	while (current != NULL)
	{
		printf("%u\n", current->n);
		n++;
		current = current->next;
	}
	return (n);
}

