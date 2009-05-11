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
	
def listobjects():
    ''' Lists all visible objects.

EFFECTS: returns a list of interactable objects like portals, doors, caves,
    tombs, boxes, and stash.
TODO: type
		filter portals, ownership, distance
    '''
    
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
    
def run(target):
    ''' Moves to a destination.

ARGUMENTS: TODO generic object?
EFFECTS: Runs towards a town portal, NPC, waypoint, player, or other object.
    '''

def enter(portal):
    ''' Enter a portal, cave, or door.

ARGUMENTS: TODO generic object?
REQUIRES: In range of portal to be used.
EFFECTS: Enters a portal/door/gate leading to another area.
    '''

def waypoint(waypoint, dest):
    ''' Take a waypoint to an area of choice.

ARGUMENTS: TODO. Waypoint is a general object? Is dest just a string
    specifying area or int,int -> act,area?
REQUIRES: Within range of a waypoint, have access to target area.
    '''