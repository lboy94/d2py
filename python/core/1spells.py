''' Select and cast spells.

You must be in-game to do this.
'''   
#
# Modifiers:
#

RIGHT,LEFT = range(2)

def select(spell, side=RIGHT):
    ''' Selects a spell.

ARGUMENTS: boolean, string
REQUIRES: You have the spell. C/I if you don't.
EFFECTS: Selects the spell on the right if true, on the left if false.
TODO: Spell list?
    '''
    
def cast(target, side=RIGHT):
    ''' Casts a spell.

ARGUMENTS: general object (TODO), int
REQUIRES: Have a castable spell selected. (Normal attack is a 'spell' too.)
EFFECTS: If right is true casts right spell, else left spell, on the target.
    '''

def cast(x, y, side=RIGHT):
    ''' Casts a spell.

ARGUMENTS: int, int, int
REQUIRES: Have a castable spell selected. (Normal attack is a 'spell' too.)
EFFECTS: If right is true casts right spell, else left spell, on a position.
    Arguments use coordinate system used by network protocol.
    '''

def weaponswitch():
    ''' Switches between primary and secondary weapon screens.

EFFECTS: This is a deceptively simple but notoriously tricky command. Doing it
    too soon after casting will fail, casting item-skills too soon after doing
    it will C/I you, and lag may delay the switch. Provided you don't do it too
    close to something, however, it should always occur. Use it carefully and
    double-check that it takes effect.
    '''
    
