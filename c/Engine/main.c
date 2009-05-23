/* 
 *   When this implementation of d2py is injected into D2, it starts
 * a thread. The mainThread() function is the body of that thread. It should
 * initialize the Python interpreter and builtins, then start the 
 * actual bot by running the main Python script.
 */
#include <Python.h>
#include <windows.h>
#include <stdio.h>
#include "options.h"
// Built-in modules:
#include "core.h"
#include "template.h"
#include "me.h"

//#define _CREATE_DEFINITIONS
#include "Pointers.h"
#undef _CREATE_DEFINITIONS
#include "Offsets.h"

#pragma comment(lib, "python30")

DWORD WINAPI mainThread(LPVOID lpArg)
{
	#ifdef MAKE_DEBUG_CONSOLE
	// Opens a console window for D2, which can be used to printf() data.
	// Might be a good idea to link the Python interpreter to this, if only
	// I knew how.
	// Then again, keeping the C core output separate may be benefitial.
	FILE* stream;
	AllocConsole();	freopen_s(&stream, "conout$", "w", stdout);	
	#endif

	printf("Main d2py thread starting in process %d.\n", GetProcessId(GetCurrentProcess()));
	
	//DefineOffsets();
	printf("Defineoffsets called.\n");

	//Py_SetProgramName("C:/Projects/2009 Summer/d2py/python/d2py.dll");
	//Py_SetProgramName("d2py.dll"); // Is this needed? Used to find the operating dir?

	// Register and initialize all modules with the Python interpreter.
	PyImport_AppendInittab("_core", PyInit_core);
	PyImport_AppendInittab("_template", PyInit_template);
	PyImport_AppendInittab("_me", PyInit_me);


	Py_Initialize();
	printf("Python interpreter and built-in modules initialized.\n");

	// Dirty hack to initialize sys.argv[0], without which tkinter fails completely.
	// We currently rely on tkinter to serve as stdout.
	//
	// Hum, using the modified PyShell script solves that problem though. What was I doing wrong?
	//PyRun_SimpleString("import sys");
	//PyRun_SimpleString("sys.argv=['C:/Projects/2009 Summer/d2py/python/d2py.dll']");


	// Setup is done: let's run the main script file.
	//
	// Using PyRun_*File functions is a terrible idea due to FILE* structure being
	// compiler-dependant. The following method looks ugly, but seems to work.
	//
	// TODO: figure out how to set the directory this stuff runs in.
	PyRun_SimpleString("exec(compile(open('C:/Projects/2009 Summer/d2py/python/d2py.py').read(), 'd2py.py', 'exec'))");
	

	// Looks like we ran out of things to do.
	printf("Main d2py thread finished, cleaning and exiting.\n");
	Py_Finalize();
	return 0;
}
