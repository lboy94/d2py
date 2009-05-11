def registercallback(hook, func):
    ''' Registers a callback function for some specific functionality.

ARGUMENTS: string, function
EFFECTS:
    '''

# Callbacks: must be registered with the core.

# ...

# These are optional, or at least lower-priority:

def chatreceived(msg):
    " New chat/whisper/friend/bnet message received."

def network.serverlag():
    ''' No data from the server for the past n seconds.

When the hook is set, an n second timeout is configured to trigger this action.
    '''

def traderequest(player):
    " Another player is asking to trade with you."

def resynchoccured():
	" Running sucks anyway, probably don't need to bother with this."