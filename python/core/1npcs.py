#
# Accessors:
#

def listnpcs():
    ''' Lists all visible NPCs.

EFFECTS: returns a large list of all visible NPCs of all types, including
    shopkeepers, noncombatants, mercenaries, monsters, and corpses.
TODO: type
		filter distance, flags, type

    'id':int    # generic object id
    'type':int  # always equal to 1 for NPCs, but needed for some funcs?
    'xy':(int,int)
    'hp':float
    'alive':boolean
    'hostile':boolean  # could get rid of this and let python sort it:
                        # there's probably an easy in-game flag, but packets...
    'type':string   # boss/unique/normal/shopkeep?
    'name':string   # npc name
    'properties':['fanatic','cold enchanted','cold resistant']
    
    '''
