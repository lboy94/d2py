// Sample code for a simple built-in module.
// 
// Three sections:
//	Name, where basic information about the module is set.
//	Methods, where C functions are wrapped in Python data structures.
//	Setup, where structures are filled with information and an
//		initialization function is defined.
// Creates a new module called 'template', which can be added to the builtin 
// namespace by calling PyImport_AppendInittab("template", PyInit_template)
// before Py_Initialize() is called. PyInit_template is, naturally, an 
// initialization function.
//
#include <Python.h>
#include "module.h"

//////////////////
// Name: not a string!
#define MODULE template

//////////////////
// Methods:

// Example C function that we'd like to expose to Python scripts we run.
int test(int i) {printf("The C code may use a different stdout from Python!!!\n", i); return ++i;}
// Wrapper called py_test for the above function.
PY_WRAPPER(test)
{
  int i;
  if (!PyArg_ParseTuple(args, "l", &i))
	  return NULL;
  return Py_BuildValue("l", test(i));
}


//////////////////
// Setup:

static PyModuleDef MODULE_DEF;
// The interpreter will initialize the module by calling this function. 
// It should be registered with the interpreter by calling: 
//	PyImport_AppendInittab("yourmodulenamehere", PyInit_yourmodulename);
// This can and should be done before PyInitialize() is called.
//
// ASIDE: Python 2.x used to use PyImport_AddModule("name") followed by 
//	PyModule_Create(&module). The change in 3.x essentially gives the C
//	code a constructor - nice. (Wonder if there's a destructor too?)
PyMODINIT_FUNC PyInit_template(void) {
	// Perform C-specific setup.
	// ...
	// Perform Python-specific setup.
	return PyModule_Create(&MODULE_DEF);
}

// List of methods exported by the module.
static PyMethodDef MODULE_METHODS[] = {
// Format:
//	FUNC(string name, name, number of args, __doc__ string),
	FUNC("test", test, 1, "Returns n+1."),
	// end of list marker
	{NULL,	NULL} 
};

// Information about the module itself:
static struct PyModuleDef MODULE_DEF = {
   PyModuleDef_HEAD_INIT, MODULE_NAME,	
   "Exports a single function, test(n).", // __doc__ string
   -1,       // size of per-interpreter state of the module,
             //   or -1 if the module keeps state in global variables. 
   MODULE_METHODS
};

