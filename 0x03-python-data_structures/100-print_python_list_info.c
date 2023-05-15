#include "lists.h"

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to PyObject / list object
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i = 0;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	while (i < size)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
		i++;
	}
}
