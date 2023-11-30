#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list:linkedList
 * Return:0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list->next;

	if (list == NULL)
		return (0);
	while (slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
