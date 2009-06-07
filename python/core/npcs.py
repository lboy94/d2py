#
# Accessors:
#

npcs = {}

def _nolongerused():
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
    'quality':string   # boss/unique/normal/shopkeep?
    'name':string   # npc name
    'properties':['fanatic','cold enchanted','cold resistant']
    
    '''
    import _npcs
    return _npcs.listnpcs()

def _unsafeupdate(id):
    # update parsed list
    if _master.get(id)==None:
        del npcs[id]
        return
    from copy import deepcopy
    npcs[id] = deepcopy(_master[id])

    # parse d2 enums -> strings
    npc = npcs[id]
    
    enum = npc['name']
    if enum<len(data.npcs.npcs): npc['name'] = data.npcs.npcs[enum]
    else: npc['name'] = "Unknown "+str(n)
    
    npc['life'] = npc['life']/128

    if npc.get('state')==None:
        npc['state']='Alive'
    else:
        npc['state']=data.npcs.states[npc['state']]


def _update(id):
    ''' Internal callback function that converts entries using D2 enums into
human-readable strings. '''
    # Pretty sure unbound stdout/stderr causes print() to fail. The only
    # guaranteed way to not make interpreter flip out, is to just 'pass'
    try:
        _unsafeupdate(id)
    except:
        pass


import _npcs, data.npcs
# Get the master NPC list.
_master = _npcs.listnpcs()
# Register a hook that'll get called when master changes.
_npcs.hookupdate(_update)

