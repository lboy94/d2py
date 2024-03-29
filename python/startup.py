
def testnamedir():
    "A useless test function."
    print('Global dir:'); dir()
    print("Name:", __name__)

def testbuiltins():
    "Tests that the built-in 'template' module functions correctly."
    print("Testing built-in 'template' module:");
    import _template
    print("\t", _template.__doc__)
    print("\t", _template.test.__doc__)
    print("\t5++ is", _template.test(5))

def npcprint():
    [print([npcs[n][m] for m in npcs[n]]) for n in npcs]
    
if __name__=='__main__':
    testnamedir()
    testbuiltins()

    # Load configuration:
    import config
    config.load()
    # Set up taskman:
    import taskman
    # TODO
    # Push first task to taskman:
    # TODO

    print('Importing core.npcs to install hook...')
    from core.npcs import npcs
    print("Ready!")
    
    
