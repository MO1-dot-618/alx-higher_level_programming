#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * insert_node - insert node to a sorted list
  * @head: head of list
  * @n: number
  * Return: address of new element
  */

listint_t *insert_node(listint_t **head, int n)
{
	listint_t *arr;

	arr = malloc(sizeof(listint_t));

	if (arr == NULL)
		return (NULL);

	arr = *head;
	if (arr->n >= n && arr->next->n <= n)

	
	return (arr);
}
