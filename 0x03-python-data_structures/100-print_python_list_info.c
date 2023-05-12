#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to PyObject / list object
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	/*Retrieves size of python list*/
	Py_ssize_t = i;
	/*Declare variable i of type Py_ssize*/
	printf("[*] Size of Python LIst = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	/*print size of memery alocated*/
	for (i = 0; i < size; i++)
	/*loop over items in python list*/
	{
		PyObject *item = PyList_GetItem(p, i);
		/*items in list retrived*/
		const char *typeName = Py_TYPE(item)->tp_name;
		/*name of item*/
		printf("Element %ld: %s\n", i, typeName);
		/*print the index and type name*/
	}
}
