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
    print("Function not implemented!")
	
def listobjects():
    ''' Lists all visible objects.

EFFECTS: returns a list of interactable objects like portals, doors, caves,
    tombs, boxes, and stash.
TODO: type
		filter portals, ownership, distance

    'id':int    # generic object id
    '''
    print("Function not implemented!")
    
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
    # id (byte) x (word) y (word)
    import _me, core.me
    from core import recvGame
    run = pack("<BHH", 0x03, x, y)
    cx, cy = core.me.position()
    # id (byte) type (byte, player==0), id (uint
    spoof = pack("<BBIBHHBHH", 0x0F, 0, _me.id(), 0x17, x, y, 0, cx, cy)
    sendGame(run)
    recvGame(spoof)
    
#def run(target):
    ''' Moves to a destination.

ARGUMENTS: TODO generic object?
EFFECTS: Runs towards a town portal, NPC, waypoint, player, or other object.
    '''
#    print("Function not implemented!")

def enter(portal):
    ''' Enter a portal, cave, or door.

ARGUMENTS: TODO generic object?
REQUIRES: In range of portal to be used.
EFFECTS: Enters a portal/door/gate leading to another area.
    '''
    print("Function not implemented!")

def waypoint(waypoint, dest):
    ''' Take a waypoint to an area of choice.

ARGUMENTS: TODO. Waypoint is a general object? Is dest just a string
    specifying area or int,int -> act,area? What about bringing your merc along?
REQUIRES: Within range of a waypoint, have access to target area.
    '''
    print("Function not implemented!")

from struct import pack
from _core import sendGame

