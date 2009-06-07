''' Select and cast spells.

You must be in-game to do this.
'''   
#
# Modifiers:
#

# Which skills are currently selected:
selected = {True:'Unknown', False:'Unknown'}

def select(skill, right=True):
    ''' Selects a skill.

ARGUMENTS: string, boolean. Skill should be listed in core.data.skills[]!
REQUIRES: You have the spell. Probable C/I if you don't.
EFFECTS: Selects the spell on the right if true, on the left if false.
    '''
    import core.data # Could do this check as an assertion: this would remove
    # it when __debug__ is set to false when invoking the interpreter.
    if not skill in core.data.skills: raise TypeError('no such skill:',skill)

    if selected[right]==skill: return
    else selected[right]=skill

    sideid = {True:0x0000, False:0x8000}
    s = sideid[side]
    
    packet = pack("<BHHI", 0x3C, core.data.skills.index(skill), s, 0xFFFFFFFF)
    sendGame(packet)


def cast(x, y, side=True):
    ''' Casts a skill.

ARGUMENTS: int, int, int
REQUIRES: Have a castable spell selected. (Normal attack is a 'spell' too.)
EFFECTS: If right is true casts right spell, else left spell, on a position.
    Arguments use coordinate system used by network protocol.
    '''
    sideid = {True:0x0C, False:0x05}
    
    packet = pack("<BHH", sideid[side], x, y)
    sendGame(packet)

    
def cast(target, side=True):
    ''' Casts a skill.

ARGUMENTS: general object (TODO), int
REQUIRES: Have a castable spell selected. (Normal attack is a 'spell' too.)
EFFECTS: If right is true casts right spell, else left spell, on the target.
    '''
    sideid = {True:0x0D, False:0x06}
    
    packet = pack("<BII", sideid[side], target['type'], target['id'])
    sendGame(packet)

    
def weaponswitch():
    ''' Switches between primary and secondary weapon screens.

EFFECTS: This is a deceptively simple but notoriously tricky command. Doing it
    too soon after casting will fail, casting item-skills too soon after doing
    it will C/I you, and lag may delay the switch. Provided you don't do it too
    close to something, however, it should always occur. Use it carefully and
    double-check that it takes effect.
    '''
    raise NotImplementedError 

from _core import sendGame
from struct import pack
