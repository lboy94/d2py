''' See where you are, what your status and attributes are, and say things.

Must be in-game.
'''
#
# Accessors:
#

#def whoami():
#    ''' Describes us, the player.
#
#EFFECTS: 
#    May need to include mercenary.
#    Could later include skill+stat distribution.
#
#    'xy':(int,int)
#    'hp':int
#    'mp':int
#    'id':int
#    'area':string    
#    '''


def position():
    ''' Gives an XY position of the player.

EFFECTS: returns the xy coordinate location in tuple form.
    '''
    return _me.position()

def location():
    ''' Locates the player in the world.

EFFECTS: returns a string specifying the act and area the player is in.
    '''
    from data import areas
    return areas.levels[_me.location()]

def id():
    ''' Returns the player ID.

EFFECTS: returns an unsigned int specifying the player's unique identifier.
TODO: remove this in favor of a stat[] dictionary or something
    '''
    return _me.id()

# Can't be filled on startup: must be passed to C via call in startup,
# then filled when the data becomes available?
# WARNING: delayed initialization
stat = {
    'id':12345,
    'name':'Johnny',
    'class':'Sorceress',
    'level':99,
    'stats':{'str':10, 'dex':10, 'vit':10, 'energy':90},
    'skills':{'Fire Ball':20}
    }


def mercenary():
    "Return merc id?"
    pass


#
# Modifiers, instant:
# 

# Note: might move this to core.chat once chat callback/buffer is done?
def chat(message):
    ''' Chats, overhead chats, whispers, and sends battle.net commands.

ARGUMENTS: string
EFFECTS: Functions like in-game chat, with ! doing overhead chats / invoking
    battle.net commands and everything else being said in chat.
    '''
    from struct import pack
    from _core import sendGame
    
    if message[0]=='!':
        # Overhead chat
        msg = message[1:]
        # packet id (byte) unknown (word, 0) message (str) blank (str) (str)
        packet = pack("<BH"+str(len(msg))+"sBBB", 0x14, 0, msg, 0, 0, 0)
        sendGame(packet)
        pass
    elif message[0]=='/':
        # Bnet command
        print("Bnet command sending not implemented!")
        pass
    elif message[0]=='@':
        # In-game whisper
        #
        # Eg: 15 02 00[74 65 73 74 79 00][62 6F 67 65 6E 5F 4C 65 78 69 00]00
        # id (byte) mtype (word, 2) message (str) charname (str) empty (str)
        msg = message[1:].strip() # cut off the @ and lead/trail spaces
        name = msg.split(' ')[0] # get first word, the target character name
        msg = msg[len(name)+1:] # cut off character name leaving message
        # byte short string string string
        packet = pack("<BH"+str(len(msg))+"sB"+str(len(name))+"sBB",
                                            0x15, 2, msg, 0, name, 0, 0)
        sendGame(packet)
        pass
    else:
        # Normal chat packet.
        #
        # Example: 15 01 00[68 65 68 65 65 5D 23 00]00 00
        # id (byte) mtype (word, 2) message (str) empty (str) empty (str)
        packet = pack("<BH"+str(len(message))+"sBBB", 0x15, 1, message, 0, 0, 0)
        sendGame(packet)
	
#
# Callbacks:
#
def hpmpchange(hp, mp):
    ''' Notifies of an hp or mp change.
    '''
    print("Function not implemented!")

# Built-in module that carries many of the implementations we'll use:
import _me
