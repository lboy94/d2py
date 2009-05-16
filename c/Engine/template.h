#ifndef _TEMPLATE_H_
#define _TEMPLATE_H_

// The interpreter will initialize the module by calling this function. 
//
// It should be registered with the interpreter by calling: 
//	PyImport_AppendInittab("yourmodulenamehere", PyInit_yourmodulename);
// This can and should be done before PyInitialize() is called.
PyMODINIT_FUNC PyInit_template(void);

//Sample usage once initialized:
//	>>> import template
//	>>> dir(template)
//	['__doc__', '__name__', '__package__', 'test']
//	>>> template.__doc__
//	'Exports a single function, test(n).'
//	>>> template.test.__doc__
//	'Returns n+1.'
//	>>> template.test(5)
//	6
//	>>> 



#endif