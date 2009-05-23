''' Move through the world, view static world objects.
	
Must be in-game.
Pathing is a separate can of worms.
'''
#
# Accessors:
#

def listwaypoints():
    ''' Lists all available waypoints.

EFFECTS: returns a list of areas accessible with waypoint system; or, if
    waypoint has not been interacted with, returns an empty list.
TODO: type
    '''
    raise NotImplementedError 
	

def listobjects():
    ''' Lists all visible objects.

EFFECTS: returns a list of interactable objects like portals, doors, caves,
    tombs, boxes, and stash.
TODO: type
		filter portals, ownership, distance

    'id':int    # generic object id
    '''
    raise NotImplementedError 

    
#
# Modifiers:
#

def run(x,y):
    ''' Moves to a destination.

ARGUMENTS: int, int
EFFECTS: Runs towards the destination. Arguments use coordinates used by network
    protocol. (Increasing Y axis to the SW, X axis to the SE, probable unit of
    yards.)
    '''
    # I'll use the packet-method. Sheppard's ClickMap wrapper in d2bs is nice,
    # but not caring about screen size is nicer. It's not like this is 'hard' :p
    #
    # This may desynch when minimized. That can be fixed by spamming fake
    # (or even real) resynch packets, which, since Kukbot uses it, seems to be
    # the most stable method.
    #
    import _me, core.me
    #TODO: using this syntax adds recvGame to the export list of this module
    # find a way to fix this, is __all__ the correct method?
    from _core import recvGame
    # id (byte) x (word) y (word)
    run = pack("<BHH", 0x03, x, y)
    cx, cy = core.me.position()
    # id (byte) type (byte, player==0), id (dword), movetype (byte),
    #   dest x, dest y (word, word), unused (byte, 0), start x, y (word, word)
    spoof = pack("<BBIBHHBHH", 0x0F, 0, _me.id(), 0x17, x, y, 0, cx, cy)
    sendGame(run)
    recvGame(spoof)
    
#def run(target):
    ''' Moves to a destination.

ARGUMENTS: TODO generic object?
EFFECTS: Runs towards a town portal, NPC, waypoint, player, or other object.
    '''
#    raise NotImplementedError 

def enter(portal):
    ''' Enter a portal, cave, or door.

ARGUMENTS: TODO generic object?
REQUIRES: In range of portal to be used.
EFFECTS: Enters a portal/door/gate leading to another area.
    '''
     raise NotImplementedError 


def waypoint(waypoint, dest):
    ''' Take a waypoint to an area of choice.

ARGUMENTS: TODO. Waypoint is a general object? Is dest just a string
    specifying area or int,int -> act,area? What about bringing your merc along?
REQUIRES: Within range of a waypoint, have access to target area.
    '''
    raise NotImplementedError 


from struct import pack
from _core import sendGame

