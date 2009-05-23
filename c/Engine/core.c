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

#define MODULE core
#include <Python.h>
#include "module.h"
#include "keysender.h"
#include "packetsender.h"

//////////////////
// Name: not a string!

//////////////////
// Methods:

PY_WRAPPER(write)
{
	char* str; 
	if (!PyArg_ParseTuple(args, "s", &str))
	  return NULL;

	typeText(str);

	return Py_BuildValue(""); // return None
}

PY_WRAPPER(sendGame)
{
	char* buff;
	int size ;  
	if (!PyArg_ParseTuple(args, "y#", &buff, &size))
	  return NULL;

	sendGame((unsigned char*)buff, size);

	return Py_BuildValue(""); // return None
}

PY_WRAPPER(recvGame)
{
	char* buff;
	int size ;  
	if (!PyArg_ParseTuple(args, "y#", &buff, &size))
	  return NULL;

	recvGame((unsigned char*)buff, size);

	return Py_BuildValue(""); // return None
}

//////////////////
// Setup:


// List of methods exported by the module.
static PyMethodDef MODULE_METHODS[] = {
// Format:
//	FUNC(string name, name, number of args, __doc__ string),
	FUNC("write", write, 1, "Write a string of characters to the D2 process, as if from a keyboard.\
	There are limitations: for example, trying to chat while in-game using this method will fail when \
	minimized due to D2 not updating the chat buffer state when the game is minimized."),
	FUNC("sendGame", sendGame, 1, "Send a packet to the game server."),
	FUNC("recvGame", recvGame, 1, "Spoof a packet to the client from the server."),
	// end of list marker
	{NULL,	NULL} 
};

// Information about the module itself:
static struct PyModuleDef MODULE_DEF = {
   PyModuleDef_HEAD_INIT, MODULE_NAME,	
   "Collection of functions for manipulating the D2 process.", // __doc__ string
   -1,       // size of per-interpreter state of the module,
             //   or -1 if the module keeps state in global variables. 
   MODULE_METHODS
};

// The interpreter will initialize the module by calling this function. 
// It should be registered with the interpreter by calling: 
//	PyImport_AppendInittab("yourmodulenamehere", PyInit_yourmodulename);
// This can and should be done before PyInitialize() is called.
//
// ASIDE: Python 2.x used to use PyImport_AddModule("name") followed by 
//	PyModule_Create(&module). The change in 3.x essentially gives the C
//	code a constructor - nice. (Wonder if there's a destructor too?)
PyMODINIT_FUNC PyInit_core(void) {
	// Perform C-specific setup.
	// ...
	// Perform Python-specific setup.
	return PyModule_Create(&MODULE_DEF);
}
