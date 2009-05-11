''' List games you can see, join them, or make new ones.

You must be logged in, character selected, and not allready in-game.

'''

#
# Accessors:
#

def listgames():
    ''' Lists games your character can see.

EFFECTS: Requests a list of games, then waits for a response to arrive.
TODO: type, blocking/nonblocking?
        iterator games
		filter players, duration, name
	'''
	
#
# Modifiers:
#

def make(name, password, difficulty="Hell", maxlevel=99, maxplayers=8):
    ''' Makes a new game.

ARGUMENTS: string, string, string, int, int
EFFECTS: creates and joins a new game called name.
TODO: failure?
    '''
    
def join(name):
    ''' Joins an existing game.

ARGUMENTS: string
EFFECTS: joins the existing game called name.
TODO: failure?
    '''