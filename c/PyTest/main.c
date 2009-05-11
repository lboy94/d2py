#include <Python.h>
#include <windows.h>

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
void init_pyextension()
{
  PyImport_AddModule("durp");
  PyModule_Create(&durp_module);

  //Py_InitModule("durp", durp_methods);
}

PyMODINIT_FUNC
PyInit_durp(void)
{
	return PyModule_Create(&durp_module);
}

DWORD WINAPI runPython(LPVOID lpArg)
{	
	FILE* fp;
	PyObject *mod, *dict, *fa, *fac, *fb, *fbc;
	void* p;
	FILE* stream;

	AllocConsole();
	freopen_s(&stream, "conout$", "w", stdout);	
	printf("Thread starting in process %d.\n", GetProcessId(GetCurrentProcess()));

	PyImport_AppendInittab("durp", PyInit_durp);
	Py_SetProgramName("d2py.exe");
	Py_Initialize();
	
	//mod = PyImport_ImportModule("sys");
	//dict = PyModule_GetDict(mod);
	//PyObject_SetAttrString(dict, "argv[0]", Py_BuildValue("s", "C:/Projects/2009 Summer/d2py/python/d2py.dll"));
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.argv=['C:/Projects/2009 Summer/d2py/python/d2py.dll']");
	//init_pyextension();
	/*
	mod = PyImport_ImportModule("d2py");
	dict = PyModule_GetDict(mod);
	fa = PyObject_GetAttrString(mod, "a");
	fac = PyObject_GetAttrString(fa, "__call__");
	fb = PyObject_GetAttrString(mod, "b");
	fbc = PyObject_GetAttrString(fb, "__call__");
	*/
	PyRun_SimpleString("print('stillalive')");
	
	PyRun_SimpleString("exec(compile(open('C:/Projects/2009 Summer/d2py/python/d2py.py').read(), 'd2py.py', 'exec'))");
	
	return 0;
}

int main(int argc, char* argv[])
{
	HANDLE hThread;
	int threadId;
	hThread = CreateThread(NULL, // lpThreadAttributes
			0,	// dwStackSize
			runPython, // lpStartAddress
			NULL, // lpParameter
			0, // dwCreationFlags (0==run right after creation)
			&threadId
		);
	Sleep(100000);
	printf("Main exit.\n");
	return 0;
}
