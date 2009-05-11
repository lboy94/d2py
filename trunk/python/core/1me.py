''' See where you are, what your status and attributes are, and say things.

Must be in-game.
'''
#
# Accessors:
#

def whoami():
    ''' Describes us, the player.

EFFECTS: 
    May need to include mercenary.
    Could later include skill+stat distribution.

    'xy':(int,int)
    'hp':int
    'mp':int
    'id':int
    'area':string    
    '''

#
# Modifiers, instant:
# 

def chat(message):
    ''' Chats, overhead chats, whispers, and sends battle.net commands.

ARGUMENTS: string
EFFECTS: Functions like in-game chat, with ! doing overhead chats / invoking
    battle.net commands and everything else being said in chat.
    '''
	
#
# Callbacks:
#
def hpmpchange(hp, mp):
    ''' Notifies of an hp or mp change.
    '''
