#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
  * check_cycle - checks if circular
  * @list: head of list
  * Return: 1 if circ, 0 not.
  */

int check_cycle(listint_t *list)
{
	listint_t *ptr = list->next;

	while (ptr != NULL && ptr != list)
		ptr = ptr->next;
	if (ptr == list)
		return (1);
	return (0);
}
