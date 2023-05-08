#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 * Description: Floyd's Tortoise & Hare algorithm to detect cycle,
 *	slow & fast point to head but slow moves 1 step while fast moves 2 steps
 *	if cycle, fast will catch up
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
