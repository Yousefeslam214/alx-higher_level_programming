#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int *arr, len = 0, i = 0, j;
	listint_t *current;

	current = *head;
	while (current)
	{
		current = current->next;
		len++;
	}
	arr = malloc(sizeof(int) * len);
	if (!arr)
		return (0);
	for (i = 0; current; i++)
	{
		arr[i] = current->n;
		current = current->next;
	}
	for (j = 0; j < ((len / 2)); j++)
	{
		if (arr[j] != arr[len - j - 1])
		{
			free(arr);
			return (0);
			}
	}
	free(arr);
	return (1);
}
