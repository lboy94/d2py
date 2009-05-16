
def testnamedir():
    "A useless test function."
    print('Global dir:'); dir()
    print("Name:", __name__)

def testbuiltins():
    "Tests that the built-in 'template' module functions correctly."
    print("Testing built-in 'template' module:");
    import template
    print("\t", template.__doc__)
    print("\t", template.test.__doc__)
    print("\t5++ is", template.test(5))

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


    
