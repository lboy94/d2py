''' Main entry point. This is the file run by d2py.dll on injection!

    Module is loaded in __main__ namespace the moment the DLL is injected and
main thread is started. Control need not be returned, the thread is all ours.
    Main goals are to start a GUI that lets us print data to stdout/stderr since
those are not bound at interpreter startup, and do any very basic initialization
like figuring out what path all our scripts are at.
    Control will then get passed to startup.py, which handles more detailed
bot initialization.

    CAUTION: THIS MODULE IS VERY SENSITIVE TO FAILURE. ANY FAILURE THAT OCCURS
    WILL PROBABLY BE SILENT SINCE NO STDOUT HAS BEEN INITIALIZED. IT WILL ALSO
    BE FATAL.
'''

if __name__=='__main__':
    # Start IDLE gui, it will start startup.py for us.
    #TODO: sort out paths somehow.
    #   pass it to DLL in CreateRemoteThread param?
    #   find path to DLL, is it possible if LoadLibrary'd into another proc?
    #   registry lookup?
    import idleshell
    idleshell.main('C:/Projects/2009 Summer/d2py/python/startup.py')


