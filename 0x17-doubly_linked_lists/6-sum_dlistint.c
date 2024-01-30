#include "lists.h"

/**
 * sum_dlistint -  function that returns the sum of
 *                 all the data (n) of a dlistint_t linked list.
 * @head: The pointer to the doubly linked list head
 * Return: sum of all data in a list
 */

int sum_dlistint(dlistint_t *head)
{
	dlistint_t *current;
	int sum = 0;

	if (head)
	{
		current = head;
		while (current)
		{
			sum += current->n;
			current = current->next;
		}
	}
	return (sum);
}
