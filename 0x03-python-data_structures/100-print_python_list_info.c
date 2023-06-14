#include "Python.h"

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: pointer
*/

void print_python_list_info(PyObject *p)
{
    Py_ssize_t a, b;
    PyObject *c;
    const char *d;
    PyListObject *e;

    e = (PyListObject *)p;
    b = PyList_Size(p);
    printf("[*] Size of the Python List = %d\n", (int) b);
    printf("[*] Allocated = %d\n", (int)e->allocated);
    for (a = 0; a < b; a++)
    {
        c = PyList_GetItem(p, a);
        d = Py_TYPE(c)->tp_name;
        printf("Element %d: %s\n", (int) a, d);
    }
}
