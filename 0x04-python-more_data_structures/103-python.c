#include <stdio.h>
##include <Python.h>

void print_python_list(PyObject *p)
{
    //Get an iterator for the list
    PyObject *iterator = PyObject_GetIter(list);
    if (iterator == NULL)
    {
        //If the object is not iterable, return immediately
        return;
    }

    //Initialize a counter for the list elements
    Py_ssize_t = i = 0;

    //Iterate over the elements of the list
    while (1)
    {
        //Get the next element of the list
        PyObject *item = PyIter_Next(iterator);
        if (item == NULL)
        {
            //If there are no more elements, break the loop
            break;
        }
        //Print the type and value of the element
        printf("Element %ld: Type - %s, Value - ", i, item->ob_type->tp_name);
        PyObject_Print(item, stdout, Py_PRINT_RAW);
        printf("\n");

        //Increment the counter
        i++;
    }

    //Decrement the reference count of the iterator
    Py_DEREF(iterator);
}

void print_bytes_info(PyObject *bytes)
{
    //Get the size of the bytes object
    Py-ssize size = PyObject_Length(bytes);
    printf("size: %ld\n", size);

    //Get a pointer to the underlying data
    char *data = PyBytes_AsString(bytes);

    //Print the data as a hexadecimal string
    printf("Data: ");
    for(Py_ssize_t i = 0; i < size; i++)
    {
        printf("%02x ", (unsigned char)data[i]);
    }
    printf("\n");
}



