
def testbuiltins():
    #import time
    #time.sleep(1)
     
    import durp
     
    print("Testing some simple builtins:")
    print('\tGlobal dir: ',dir())
    print("\tName:", __name__)
    print('\tdurp.dir:',dir(durp))
    print('\tdurp.doc:',durp.__doc__)
    print('\tRunning functions in durp:')
    n = 1;
    for i in range(5): n = durp.inc(n)
    print('\tDone!')

if __name__=='__main__':
    # Set up config:
    # TODO
    # Set up taskman:
    # TODO
    # Push first task to taskman:
    # TODO

    testbuiltins()
