#
# Accessors:
#
def listcharacters():
    ''' Lists selectable characters.

REQUIRES: Logged in, but haven't selected a character yet.
EFFECTS: Returns a dictionary of characters on the account. Character names are
    keys, and values are (level,class,ladder,hardcore,dead,difficulty) tuples.
    Types inside tuples are (int,string,bool,bool,bool,string).
    '''
	
#
# Modifiers:
#
def startclient(path):
    ''' Starts a game client.
	
ARGUMENTS: path is a string that points to a standard game client executable.
EFFECTS: Starts the game client and hooks up to it.
    '''

def connect2bnet(realm, classic, xpac):
    ''' Connect to the Internet.

ARGUMENTS: classic and xpac are valid realm-enabled CD keys in string format,
    with no separating marks between characters. realm is a valid name string.
REQUIRES: Client started but not connected to battle.net.
EFFECTS: Connects the client to Battle.net.
TODO: failure?
    '''
	
def login(account, password):
    ''' Login to an account.

ARGUMENTS: Two case insensitive strings
REQUIRES: Connected to battle.net, not logged in.
EFFECTS: Logs on up to the character selection screen.
    '''
	
def selectcharacter(name):
    ''' Select a character.

ARGUMENTS: Case-insensitive string
REQUIRES: Logged in, character not selected.
EFFECTS: Selects the character, reaching the point where channels can be joined
    and games made.
    '''

def shutdownclient():
    ''' Closes the game client immediately.
	
EFFECTS: Closes the game client without properly logging out. If client
	allready closed, no effect.
    '''
