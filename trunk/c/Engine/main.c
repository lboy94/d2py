#include <Python.h>
#include <windows.h>
#include <stdio.h>
#include "options.h"

#pragma comment(lib, "User32")

#pragma comment(lib, "python30")

/* now a method we need to expose to Python */
long inc(long i) {
	printf("inc called on: %d\n", i);
	return ++i;
}

/* and the magic that exposes it - a builtin module */
/* first, the wrapper function */
static PyObject *py_inc(PyObject *self, PyObject *args)
{
  long i;
  if (!PyArg_ParseTuple(args, "l", &i))
      return NULL;
  return Py_BuildValue("l", inc(i));
}

/* now the module's function table */
static PyMethodDef durp_methods[] = {
  {"inc",     (PyCFunction)py_inc,     1,  "a silly example method"},
  {NULL,      NULL}       /* sentinel */
};

static struct PyModuleDef durp_module = {
   PyModuleDef_HEAD_INIT,
   "durp",   /* name of module */
   "This module is durp a durp de durp durp", /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   durp_methods
};

/* Python will call this when the module is imported */
/*void init_pyextension()
{
  PyImport_AddModule("durp");
  PyModule_Create(&durp_module);

  //Py_InitModule("durp", durp_methods);
}*/

PyMODINIT_FUNC
PyInit_durp(void)
{
	return PyModule_Create(&durp_module);
}


DWORD WINAPI mainThread(LPVOID lpArg)
{
	#ifdef MAKE_DEBUG_CONSOLE
	// Opens a console window for D2, which can be used to printf() data.
	// TODO: link Python interpreter into this.
	FILE* stream;
	AllocConsole();	freopen_s(&stream, "conout$", "w", stdout);	
	#endif

	printf("Main d2py thread starting in process %d.\n", GetProcessId(GetCurrentProcess()));
	
	//Py_SetProgramName("C:/Projects/2009 Summer/d2py/python/d2py.dll");
	//Py_SetProgramName("d2py.dll"); // Is this needed? Used to find the operating dir?
	
	PyImport_AppendInittab("durp", PyInit_durp);
	Py_Initialize();
	printf("Python interpreter and built-in modules initialized.\n");

	// Dirty hack to initialize sys.argv[0], without which tkinter fails completely.
	// We currently rely on tkinter to serve as stdout.
	//
	// Hum, using the modified PyShell script solves that problem though.
	//PyRun_SimpleString("import sys");
	//PyRun_SimpleString("sys.argv=['C:/Projects/2009 Summer/d2py/python/d2py.dll']");

	// Setup is done: let's run the main script file.
	//
	// Using PyRun_*File functions is a terrible idea due to FILE* structure being
	// compiler-dependant. The following method looks ugly, but seems to work.
	//
	// TODO: figure out what directory this stuff runs in?
	PyRun_SimpleString("exec(compile(open('C:/Projects/2009 Summer/d2py/python/d2py.py').read(), 'd2py.py', 'exec'))");
	
	/*
	PyRun_SimpleString("import durp");
	PyRun_SimpleString("durp.inc(1)");
	PyRun_SimpleString("print('durp')");
	PyRun_SimpleString("import d2py");
	PyRun_SimpleString("d2py.d2py()");
	*/

	// Looks like we ran out of things to do.
	printf("Main d2py thread finished, cleaning and exiting.\n");
	Py_Finalize();
	return 0;
}
