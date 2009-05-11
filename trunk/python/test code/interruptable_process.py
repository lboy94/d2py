'''Important idea!: have waiting+sleeping stacks for each priority. Waiting
tasks get tupled with a timer on the sleeping stack until they're ready to
prevent cpu use?

Idea: on chicken-potting, if low on pots fastTp to town to buy more pots.
'''
''' Potential exception hierarchy:
exception
    realmdown #delay a while, restart D2
    slowdown #delay a while, restart D2 to avoid R/D
    keyswap #switch keys and restart?
    gamecrash #restart D2
        gamedrop #restart game
            pathfail # drop specific boss, move to next?
        death # restart game, get corpse
        chicken # restart game, maybe get corpse
        invfull # restart game, mule gear
    showstopper # give up
        nomerc # if option set
        nopots # if no gold and option set?
        corpsefail # can't get corpse in one-two tries

'''
# Simple script that performs a typical talk to NPC -> buy potions -> id items
#   -> sell items task, with a twist.
#
# The task is performed piece by piece, returning control to a taskmaster at the
#   end of each piece. This allows the possibility of easy multitasking, at the
#   cost of slightly increased code complexity!

# Critical sections that cannot be interrupted should not have any yield 
#   statements. Normal function calls may be used to ensure good quality of 
#   code, of course.
# Otherwise, tasks should be broken into small sections and 'yield' control to
#   the taskmaster every so often. No solid numbers for how often control must
#   yield exist, but if a high-priority task (like grabbing an SOJ someone
#   dropped) gets scheduled it cannot be executed until control is yielded.
# Ideally, control would be yielded at least >10 times a second.

# Note: potting and game chicken are real-time instant tasks not requiring a
#   yield.

# yield (RETURN,retval) to return a value to the caller
# yield (WAIT,ms) to pause this stack's execution for some miliseconds
# yield DONE is shorthand for returning success
# yield BUSY is shorthand for a 0ms wait, giving other tasks time to execute
#   but not adding any delay.
RETURN,WAIT = range(2)
DONE = (RETURN,True)
BUSY = (WAIT,0)

# Custom exception.
class IdentificationException(Exception): pass

# Some building-block tasks:
def identifyItems():
    '''A very simple task. It can raise an exception: exceptions get propagated
to all other tasks queued on the stack, until one handles it or there's no more
tasks left in which case the bot fails. (Exception propagate sideways to
adjacent stacks too.)
    Potential problem: what about tasks that repeat by going to the bottom of
the stack? How do you purge them in case of an exception?
    '''
    raise IdentificationException("oh no we can't identify items")
    print('Identified items.');
    yield DONE        

def sellItems():
    "Another simple task, showcasing returning some data to caller."
    print('Selling some items...');
    yield (RETURN,(2,("Enigma", "Shako")))

def buyPots():
    "A long task that yields control several times without breaking flow."
    needPots = 4;
    while needPots>0:
        print('Need %d potions. Bought one.' % (needPots));
        needPots-=1;
        yield BUSY
    yield (RETURN,4) # Note that we return # of pots bought to the caller!
    
def waitUntil(condition):
    '''Task that pauses execution until a condition is reached. Can be modified
to throw an exception if a timeout is exceeded.
    What's important, though, is that even though execution is paused other
tasks can still be checked and possibly implemented. This is far superior to
sleep() or wait() type functions.
    '''
    while False: yield BUSY # In this demo, condition immediately satisfied.
    yield DONE
    
def walkTo(dest):
    "A simple task that needs some time to complete."
    print('Walking to '+dest);
    yield waitUntil("finished walking")
    yield DONE

# A higher-level task that calls a bunch of other tasks:
def shop():
    "A high level control block that performs a multi-step task."
    print('Going shopping.')
    yield walkTo('Malah') # <- we can pass parameters to the callee
    print('Started talking to Malah.')
    pots = yield buyPots() # <- we can get a return value too
    print('Bought a total of',pots,'pots.')
    try:
        yield identifyItems()
    except IdentificationException:
        # Handle a failure cleanly
        print("identifyItems failed but shop handled it.")
    r = yield (WAIT, 500) # <- we can wait 500ms if we want to
    sold,items = yield sellItems()
    print('sellItems sold',sold,'items:',items)
    print("Done shopping, what's next?")


#############################################################
# Task code ends, taskmaster engine begins.

# Engine helper function:
def parsecontrolcode(stack, ret):
    "Modify stack and propagate return values according to data 'yield'ed."
    if type(ret)==type(stack[-1]):
    # Generator type. Means that a new task was returned, enqueue it.
        s.append(ret)
        return None
    elif ret==None:
        raise Exception("Coroutine returned none - did you"+
                        "forget to yield DONE in a function?");
    else:
        code,retval = ret;
        if code==WAIT:
        # Either the task is waiting for retval miliseconds, or it ain't done
        #   yet, but it relinquished control so we could do something else
        #   for a moment. How nice of it!
            if retval==0:
                pass
            else:
                print('\tProcess paused for',retval,'ms.')
        elif code==RETURN:
            # Task is done, garbage collect it to avoid memory leak.
            gc = s.pop();
            del gc
        return retval
    

# Main program entrypoint:
print('INTERRUPTABLE PROCESS DEMO:')

# We want to run the shop() task.
s = [shop()]

# Initialize a variable so it doesn't get eaten by scope.
retval = None

# Loop over a stack (just one, in this case) until empty:
try:
    while len(s)>0:
        # Print a stack trace. Control is in our hands: we can do other things
        #   like checking other priority stacks.
        print("\tStack:", [x.__name__ for x in s])
        try:
            # Execute the topmost task.
            if isinstance(retval, Exception):
                ret = s[-1].throw(retval)
            else:
                ret = s[-1].send(retval)
            # It will return a control code basedon which we control the stack.
            retval = parsecontrolcode(s, ret)
        except StopIteration as e:
            # hack to end the main loop
            raise e 
        except Exception as e:
            # Gc failed task.
            gc = s.pop();
            print('\tTask',gc.__name__,'raised exception:',e)
            del gc
            # Propagate exception through stack.
            retval = e
except StopIteration:
    print("\tTask buffer empty, all tasks finished.")


# No longer used.
def testException(func):
    ''' Test if a task coroutine conforms to the exception propagation
requirement.
    '''
    try:
        f = func()
        f.throw(Exception('passed the exception propagation test.'))
    except Exception as e:
        print(func.__name__,e)
        return True
    print('Error:',func.__name__,'failed the exception propagation test.')
    return False


''' Use yield to push additional tasks on the stack. goShop() could yield
goTo(Malah) then waitForDestination(10 seconds) then chat(Malah) then buyPots()
then identifyItems() then sellItems() then buyScrolls then it does
stopInteraction and exits.

send the return from the called function to the caller, so data is passed.
Can use tuples to pass lots of data per call.

Idea: put shopbot into high priority stack. If it sees a nice item, it buys it.
'''
