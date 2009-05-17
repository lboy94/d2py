#ifndef _MODULE_H_
#define _MODULE_H_
// A bunch of shorthand and templating for faster builtin module writing.

// Modules should define MODULE as the module name. (Not a string.)
#define MODULE_DEF MODULE##Definition
#define MODULE_METHODS MODULE##Methods
#define QUOTEME(x) #x
#define MODULE_NAME QUOTEME(MODULE)

// All Python-wrapped functions look the same: may as well make a shortcut for it.
#define PY_WRAPPER(func) static PyObject *py_##func##(PyObject *self, PyObject *args)

// Shortens the entries in the MODULE_METHODS table a bit.
#define FUNC(str,name,args,doc) {str, (PyCFunction)py_##name##, args, doc}

#endif