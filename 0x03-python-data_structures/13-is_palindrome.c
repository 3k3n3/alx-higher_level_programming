#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to pointer to head node
 *
 * Return: void
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *curr = *head;
	listint_t *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - check if list is a palindrome
 * @head: pointer to head
 *
 * Return: 1 if palindrome, if not 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *prev_slow_ptr = *head;
	listint_t *second_half = NULL;
	int is_palindrome = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		/* Find the middle node of the list */
		while (fast_ptr != NULL && fast_ptr->next != NULL)
		{
			fast_ptr = fast_ptr->next->next;
			prev_slow_ptr = slow_ptr;
			slow_ptr = slow_ptr->next;
		}
		/* If the list has odd number of nodes, skip the middle node */
		if (fast_ptr != NULL)
			slow_ptr = slow_ptr->next;
		/* Reverse the second half of the list */
		second_half = slow_ptr;
		reverse_list(&second_half);
		/* Compare the first half and reversed second half of the list */
		while (second_half != NULL)
		{
			if (prev_slow_ptr->n != second_half->n)
			{
				is_palindrome = 0;
				break;
			}
			prev_slow_ptr = prev_slow_ptr->next;
			second_half = second_half->next;
		}
		/* Restore the original list by reversing the second half again */
		reverse_list(&slow_ptr);
		prev_slow_ptr->next = slow_ptr;
	}

	return (is_palindrome);
}
