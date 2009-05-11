''' This is ugly and needs fixin'
'''

def interact(target, goal="default"):
    ''' Interacts with a map object, NPC, player, or item.

ARGUMENTS: type varies
REQUIRES: object|npc is within interaction range, player is in town, portal book
    is not used in town. After interaction is finished stopinteraction() must be
    called.
EFFECTS:
    If target is a map object:
        Interact with it.
        
    If target is an NPC:
        First interact call starts a conversation.
        Second interact call after a successful interaction depends on goal,
with possible goals being 'trade', 'identify', 'repair', 'imbue', and 'socket'.

    If target is a player:
        Trade request is sent.

    If target is an item:
        If item is a potion:
            Drink it.
        If item is a cube:
            Cube items inside.
        If item is a portal book|scroll:
            Use it.
        If item is an identify book|scroll:
            Use it. Second interact call will identify an item.
        
TODO: is special interaction needed to get healing from Malah/Akara?
    '''

def stopinteraction():
    ''' Stops interacting with a target.

EFFECTS: Cancels any existing interaction. If not in an interaction, there are
    no negative effects.
    '''


