'''Entry point into the bot.

    Module is loaded in __main__ namespace the moment the DLL is injected and
main thread started.
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


if __name__=='__main__':
    import idleshellhack
    idleshellhack.main('C:/Projects/2009 Summer/d2py/python/run.py')


