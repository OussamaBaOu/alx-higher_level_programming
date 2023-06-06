#include <stddef.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted linked list
 * @head: linked list
 * @number: number to insert
 * Return: address of new node, or NULL if fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *a;
	listint_t *b;

	b = *head;
	a = malloc(sizeof(listint_t));
	if (a == NULL)
		return (NULL);
	a->n = number;
	if (*head == NULL || (*head)->n > number)
	{
		a->next = *head;
		*head = a;
		return (a);
	}
	while (b->next != NULL)
	{
		if ((b->next)->n >= number)
		{
			a->next = b->next;
			b->next = a;
			return (a);
		}
		b = b->next;
	}
	b->next = a;
	a->next = NULL;
	return (a);
}
