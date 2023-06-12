#include "lists.h"

/**
 * reverse - reverses second half of list
 * @a: head of second half
 */

void reverse(listint_t **a)
{
	listint_t *b;
	listint_t *c;
	listint_t *d;

	b = NULL;
	c = *a;
	while (c != NULL)
	{
		d = c->next;
		c->next = b;
		b = c;
		c = d;
	}
	*a = b;
}

/**
 * compare - compares each int of list
 * @a: head of first half
 * @b: head of second half
 * Return: 1 if equals, 0 if not
 */

int compare(listint_t *a, listint_t *b)
{
	listint_t *c;
	listint_t *d;
	c = a;
	d = b;
	while (c != NULL && d != NULL)
	{
		if (c->n == d->n)
		{
			c = c->next;
			d = d->next;
		}
		else
		{
			return (0);
		}
	}
	if (c == NULL && d == NULL)
	{
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer
 * Return: 0 if it is not a palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *a, *b, *c, *d, *e;
	int f;

	a = b = c = *head;
	e = NULL;
	f = 1;
	if (*head != NULL && (*head)->next != NULL)
	{
		while (b != NULL && b->next != NULL)
		{
			b = b->next->next;
			c = a;
			a = a->next;
		}
		if (b != NULL)
		{
			e = a;
			a = a->next;
		}
		d = a;
		c->next = NULL;
		reverse(&d);
		f = compare(*head, d);
		if (e != NULL)
		{
			c->next = e;
			e->next = d;
		}
		else
		{
			c->next = d;
		}
	}
	return (f);
}
