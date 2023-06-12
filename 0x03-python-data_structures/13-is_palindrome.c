#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * rev_listint - reverses singly-linked list
 * @head: pointer to starting node of list
 * Return: pointer to head
 */

listint_t *rev_listint(listint_t **head)
{
	listint_t *a = *head;
	listint_t *next;
	listint_t *b = NULL;

	while (a)
	{
		next = a->next;
		a->next = b;
		b = a;
		a = next;
	}
	*head = b;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer
 * Return: 0 if not palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *a, *b, *c;
	size_t e = 0;
	size_t d;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	a = *head;
	while (a)
	{
		e++;
		a = a->next;
	}
	a = *head;
	for (d = 0; d < (e / 2) - 1; d++)
		a = a->next;
	if ((e % 2) == 0 && a->n != a->next->n)
		return (0);
	a = a->next->next;
	b = rev_listint(&a);
	c = b;
	a = *head;
	while (b)
	{
		if (a->n != b->n)
			return (0);
		a = a->next;
		b = b->next;
	}
	rev_listint(&c);
	return (1);
}
