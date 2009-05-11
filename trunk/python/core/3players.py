''' Observe and hostile/party other players.

You must be in-game to do this.
'''

# 
# Accessors:
#

def listplayers():
    ''' Lists all in-game players.

EFFECTS: returns a list of all in-game players.
TODO: type
		filter attitude, distance, class?
    '''

#
# Modifiers:
# 

# Player relations
def setstatus(player,status):
    ''' Sends out party invites and hostiles players.

ARGUMENTS: TODO, string. Possible status values: "invite", "hostile", "exclude",
    "include".
REQUIRES: must hostile in town, cannot invite existing party members
EFFECTS: Invite and hostile send out invites and hostile the player,
    respectively. Exclude prevents the player from hearing you speak: include
    allows them to hear you again.
    '''

def playerchange(player, action):
    ''' Notifies that a player has changed state.

ARGUMENTS: standard player key:value dictionary, string
EFFECTS: Action might be "join"|"leave"|"party"|"unparty". Party can be any,
    not necessarily one you're in.
	'''