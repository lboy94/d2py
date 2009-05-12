''' Main entry point. This is the file run by d2py.dll on injection!

    Module is loaded in __main__ namespace the moment the DLL is injected and
main thread is started. Control need not be returned, the thread is all ours.
    Main goals are to start a GUI that lets us print data to stdout/stderr since
those are not bound at interpreter startup, and do any very basic initialization
like figuring out what path all our scripts are at.
    Control will then get passed to startup.py, which handles more detailed
bot initialization.
'''

def test():
    "A useless test function that checked if some stuff worked."
    import time
    time.sleep(1)
    #import durp
    print("d2py.py called!\n--------------")
    print('Global dir: ',dir())
    print("Name:", __name__)
    #print('durp.dir:',dir(durp))
    #print('durp.doc:',durp.__doc__)
    print('Running functions in durp:')
    n = 1;
    #for i in range(5):
    #    n = durp.inc(n)


# Currently unused, using modified copy of idlelib/PyShell.py
def myGui():
    "Provide stdin/out/err access via a slapped together gui."
    # Initialize our only means of communicating with the user.
    from gui import Gui
    gui = Gui()
    # Tk requires the main thread to update the GUI. Still not really sure why.
    # Going to humour it by running all the real work in an offshoot
    import _thread
    _thread.start_new(main, ())
    gui.mainloop() # This loop exits when the Tk console window closes.

# Main bot entry point.
if __name__=='__main__':
    # Start IDLE gui, it will start startup.py for us.
    #TODO: sort out paths somehow.
    #   pass it to DLL in CreateRemoteThread param?
    #   find path to DLL, is it possible if LoadLibrary'd into another proc?
    #   registry lookup?
    import idleshellhack
    idleshellhack.main('C:/Projects/2009 Summer/d2py/python/startup.py')


