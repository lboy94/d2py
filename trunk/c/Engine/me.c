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
#define MODULE me

#include <Python.h>
#include "module.h"
#include "Functions.h"
#include "Pointers.h"
#include "Structs.h"
#include "Levels.h"
//#include "Sender.h"
//#include "keysender.h"
//////////////////
// Name: not a string!

//////////////////
// Methods:

PY_WRAPPER(position)
{
	UnitAny* me;
	me = GetPlayerUnit();
	printf("Got UnitAny: %x\n", me);
	printf("XY: %d:%d\n",me->wX,me->wY);
	//printf("GetUnit?: %d, %d\n", GetUnitX(
	return Py_BuildValue("(l,l)",me->wX,me->wY);
}`

PY_WRAPPER(location)
{
	UnitAny* me;
	me = GetPlayerUnit();
	printf("Got UnitAny: %x\n", me);
	Room1 *pRoom = GetRoomFromUnit(me);
	DWORD lvl;
	if(pRoom && pRoom->pRoom2 && pRoom->pRoom2->pLevel)
		lvl = pRoom->pRoom2->pLevel->dwLevelNo;
	else 
		lvl = 0; // unknown
	printf("Location ID: %d, or %s\n", lvl, levelTable[lvl]);
	return Py_BuildValue("s",levelTable[lvl]);
}

PY_WRAPPER(id)
{
	UnitAny* me;
	me = GetPlayerUnit();
	printf("Got UnitAny: %x\n", me);
	
	return Py_BuildValue("I",me->dwUnitId);
}


/*
PY_WRAPPER(chat)
{
	char* str; 
	if (!PyArg_ParseTuple(args, "s", &str))
	  return NULL;

	// Assumes chat window starts closed.
	typeText("\r"); 
	Sleep(200);
	typeText(str);
	Sleep(200);
	typeText("\r");

	//sendKeyString(wnd, str);

	//switch(str[0]) {
	//case '!':
	//	overheadChat(str+1);
	//break;
	//case '/':
	//	overheadChat(str+1); // Not implemented~~
	//break;
	//default:
	//	gameChat("asdfabcd", 0, str);
	//}

	return Py_BuildValue("l", 1);
}
*/

//////////////////
// Setup:

// List of methods exported by the module.
static PyMethodDef MODULE_METHODS[] = {
// Format:
//	FUNC(string name, name, arg flags, __doc__ string),
	FUNC("position", position, 1, "Gives an XY position of the player."),
	FUNC("location", location, 1, "Locates the player in the world."),
	FUNC("id", id, 1, "Gets the player id."),
	////FUNC("chat", chat, 1, "Chats, overhead chats, whispers, and sends battle.net commands."),
	// end of list marker
	{NULL,	NULL} 
};

// Information about the module itself:
static struct PyModuleDef MODULE_DEF = {
   PyModuleDef_HEAD_INIT, MODULE_NAME,	
   "See where you are, what your status and attributes are, and say things.", // __doc__ string
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
PyMODINIT_FUNC PyInit_me(void) {
	// Perform C-specific setup.
	// ...
	// Perform Python-specific setup.
	return PyModule_Create(&MODULE_DEF);
}
