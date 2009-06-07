//////////////////
// Name: not a string!
#define MODULE npc

#include <Python.h>
#include "module.h"
#include <Windows.h>
//////////////////
// Methods:
#define getDWORD(Pointer) *(unsigned int*)(Pointer)
#define getWORD(Pointer) *(unsigned short*)(Pointer)
#define getSTR(Pointer) (char*)(Pointer)

// TODO: clear the list on conn drop
PyObject* npcs;

static PyObject *updateCallback = NULL;

// Pile of helper functions that should reduce mistakes when it comes to 
int bufferOffset;
inline void setPos(int i) {bufferOffset = i;}
inline DWORD popDWORD(unsigned char* p) {DWORD ret = getDWORD(p+bufferOffset); bufferOffset+=4; return ret;}
inline WORD popWORD(unsigned char* p) {WORD ret = getWORD(p+bufferOffset); bufferOffset+=2; return ret;}
inline BYTE popBYTE(unsigned char* p) {BYTE ret = *(unsigned char*)(p+bufferOffset); bufferOffset++; return ret;}

void npcTrackerInit() 
{
	npcs = PyDict_New();
	if (npcs==NULL) {printf("Failed to create dictionary, brace yourself for errors!");}
}

PY_WRAPPER(setCallback) 
{
	printf("Setting NPC callback function.\n");
	
	PyObject *cback;
	if (!PyArg_ParseTuple(args, "O", &cback)) {
		printf("COULD NOT PARSE CALLBACK ARGUMENT!\n");
		return NULL;
	}

	// make sure argument is a function
	if (!PyCallable_Check(cback)) {
		PyErr_SetString(PyExc_TypeError, "Need a callable object!");
		return NULL;
	}
	Py_INCREF(cback);
	updateCallback = cback;
	
	Py_INCREF(Py_None);
	printf("Callback set!\n");
	return Py_None;
}


void dataUpdate(int id)
{
	// Should be called with GIL allready acquired...
	//PyGILState_STATE gstate;
	//gstate = PyGILState_Ensure();
	// PYTHON ACCESS START \/ \/ \/

	// Build arguments then call callback. No error checking for null callbacks
	// is done!
	printf("Updating data: %d\n", id);
	if (updateCallback==NULL) {printf("FATAL: updateCallback is NULL!"); return;}

	if (!PyCallable_Check(updateCallback)) {
		printf("AAAAAAAAAAAAAAAAAAAA");
		PyErr_SetString(PyExc_TypeError, "FFFFFFFFFFFFFFFFFFFFFFFFFFFFF\n");
		return;
	}

	PyObject *arglist = Py_BuildValue("(I)", id);
	PyObject *result = PyEval_CallObject(updateCallback,arglist);
	//PyObject *result = PyEval_CallFunction(updateCallback, "(I)", 1);
	Py_DECREF(arglist);
		
	if (result==NULL) {
		// This gets called from D2's internal thread. Python isn't bound to stdout/stderr. Errors get eaten.
		// This should never happen, exceptions must be handled inside the update callback and not passed on.
		printf("NPC callback failed. This should not happen - exceptions must not reach the C caller!\n");
		//PyRun_SimpleString("f=open('TEST.TXT','w'); import sys;f.write(repr(sys.exc_info()));f.close();");
		//PyObject* err = PyErr_Occurred();
		//printf("PE_Occurred: %x\n", err);		
		//PyErr_Print();		
	} else {
		Py_DECREF(result);
	}


	//if (result && PyInt_Check(result)) {
	//	retvalue = PyInt_AsLong(result);
	//}

	// Are these needed? What EXACTLY do they do?
	//Py_XDECREF(result);
	//Py_DECREF(arglist);

	// /\ /\ /\ PYTHON ACCESS RELEASE 
	//PyGILState_Release(gstate);
}




// 0xAC COMASIGNMENT assigned to a location within range of view
void newNpc(unsigned char* data, int len)
{
	setPos(1);
	DWORD id = popDWORD(data);
	WORD code = popWORD(data); // name/code: this number represents the NPC type
	WORD x = popWORD(data);
	WORD y = popWORD(data); 
	BYTE life = popBYTE(data);
	// BYTE packet length + VOID npc info unparsed

	//printf("Packet parsed: %d %d %d %d %d\n", id, code, x, y, life);

	PyGILState_STATE gstate;
	gstate = PyGILState_Ensure();
	// PYTHON ACCESS START \/ \/ \/

	PyObject* newcomer = PyDict_New();
	if (newcomer==NULL) {printf("Error: couldn't create dictionary, exceptions ahoy!\n");}

	int ret = PyDict_SetItemString(newcomer, "id", Py_BuildValue("I", id));
	ret |= PyDict_SetItemString(newcomer, "type", Py_BuildValue("I", 0x01));
	ret |= PyDict_SetItemString(newcomer, "name", Py_BuildValue("H", code));
	ret |= PyDict_SetItemString(newcomer, "xy", Py_BuildValue("(H,H)", x, y));
	ret |= PyDict_SetItemString(newcomer, "life", Py_BuildValue("B", life));

	
	ret |= PyDict_SetItem(npcs, Py_BuildValue("I", id), newcomer);
	
	// functions return 0 on success, if ret's non-zero something went wrong
	if (ret) {printf("Error: newNpc had a problem setting dictionary values!\n");}

	// /\ /\ /\ PYTHON ACCESS RELEASE 
	dataUpdate(id);
	PyGILState_Release(gstate);
}

// 0x0A LOSTSIGHT
void lostNpc(unsigned char* data, int len)
{
	DWORD id = getDWORD(data+2);

	PyGILState_STATE gstate;
	gstate = PyGILState_Ensure();
	// PYTHON ACCESS START \/ \/ \/	
	PyDict_DelItem(npcs, Py_BuildValue("I", id));
	// /\ /\ /\ PYTHON ACCESS RELEASE 
	dataUpdate(id);
	PyGILState_Release(gstate);
}

// 0x69 COMSTATEASIGN
void stateAssign(unsigned char* data, int len)
{
	setPos(1);
	DWORD id = popDWORD(data);
	BYTE state = popBYTE(data); // known states: 0x06 alive 0x08 dying 0x09 dead
	WORD x = popWORD(data);
	WORD y = popWORD(data);
	BYTE life = popBYTE(data);
	// Unknown BYTE (possibly area id) unparsed.

	PyGILState_STATE gstate;
	gstate = PyGILState_Ensure();
	// PYTHON ACCESS START \/ \/ \/	

	PyObject* p = PyDict_GetItem(npcs, Py_BuildValue("I", id));
	
	int ret = PyDict_SetItemString(p, "state", Py_BuildValue("B", state));
	ret |= PyDict_SetItemString(p, "xy", Py_BuildValue("(H,H)", x, y));
	ret |= PyDict_SetItemString(p, "life", Py_BuildValue("B", life));

	// functions return 0 on success, if ret's non-zero something went wrong
	if (ret) {printf("Error: stateAssign had a problem setting dictionary values!\n");}

	// /\ /\ /\ PYTHON ACCESS RELEASE 
	dataUpdate(id);
	PyGILState_Release(gstate);
}


// 0x6D COMSTOP
void comStop(unsigned char* data, int len)
{
	setPos(1);
	DWORD id = popDWORD(data);
	WORD x = popWORD(data);
	WORD y = popWORD(data);
	BYTE life = popBYTE(data);

	PyGILState_STATE gstate;
	gstate = PyGILState_Ensure();
	// PYTHON ACCESS START \/ \/ \/	

	PyObject* p = PyDict_GetItem(npcs, Py_BuildValue("I", id));
	
	int ret = PyDict_SetItemString(p, "xy", Py_BuildValue("(H,H)", x, y));
	ret |= PyDict_SetItemString(p, "life", Py_BuildValue("B", life));

	// functions return 0 on success, if ret's non-zero something went wrong
	if (ret) {printf("Error: comStop had a problem setting dictionary values!\n");}

	// /\ /\ /\ PYTHON ACCESS RELEASE 
	dataUpdate(id);
	PyGILState_Release(gstate);
}

void npcPackets(unsigned char* data, int len) 
{
	if (len<1) return;

	switch(data[0]) {
	case 0x0A: // 0x0A LOSTSIGHT object has left your range of view
		if (data[1]==0x01) lostNpc(data, len);
	break;
	case 0x0C: // 0x0C COMSHOWDMG

	break;
	case 0x67: // 0x67 COMMOVE

	break;
	case 0x68: // 0x68 COMTOTARGET

	break;
	case 0x69: // 0x69 COMSTATEASIGN
		stateAssign(data, len);
	break;
	case 0x6B: // 0x6B COMACTION (warriv stretching/charsi casting+hitting an anvil)

	break;
	case 0x6C: // 0x6C COMATTACK

	break;
	case 0x6D: // 0x6D COMSTOP
		comStop(data, len);
	break;
	case 0xAA: // 0xAA COMINFOADD object comes into 4 screen view

	break;
	case 0xAB: // 0xAB COMHEAL npc gained some life

	break;
	case 0xAC: // 0xAC COMASIGNMENT assigned to a location within range of view
		newNpc(data, len);
	break;
	}
}

PY_WRAPPER(listnpcs) {return npcs;}
	
PY_WRAPPER(testupdate) {dataUpdate(7); return Py_BuildValue("");}

//////////////////
// Setup:


// List of methods exported by the module.
static PyMethodDef MODULE_METHODS[] = {
// Format:
//	FUNC(string name, name, number of args, __doc__ string),
	FUNC("listnpcs", listnpcs, 1, "Returns a dictionary of visible NPCs. Uses internal enums."),
	FUNC("hookupdate", setCallback, 1, "Hooks updates of NPC list."),
	FUNC("testupdate", testupdate, 1, "Debug test."),
	// end of list marker
	{NULL,	NULL} 
};

// Information about the module itself:
static struct PyModuleDef MODULE_DEF = {
   PyModuleDef_HEAD_INIT, MODULE_NAME,	
   "Exports accessor to master NPC list. Probably callback-trigger, too.", // __doc__ string
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
PyMODINIT_FUNC PyInit_npc(void) {
	// Perform C-specific setup.
	// ...
	// Perform Python-specific setup.
	return PyModule_Create(&MODULE_DEF);
}

