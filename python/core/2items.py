''' View, pick up, move, and buy items.

You must be in-game to do these things.

'''

#
# Callbacks:
#

def itemdropped(item):
    " Notifies that an item has been dropped."

#
# Accessors:
#

def listitems():
    ''' Lists all visible items.

EFFECTS: returns a list of items on the ground, on other players, in shops, on
    monsters, or in inventory buffers.
TODO: type
		filter ownership, type, quality, condition, etc
			(ownership includes ground, store)
			(condition filter used for repairs)

    'id':int    # generic object id
    'type':int  # items are 3 or whatever: need to have this for some funcs?
    'location':x is in:
        --- worn by someone
        amulet, body, right primary, left primary, right secondary,
        left secondary, right ring, left ring, belt, feet, gloves
        --- owned by me
        inventory, potion belt, cube, stash, my trade
        --- shop
        shop    # need to handle different pages or not?
        --- ground
        ground
        --- being held
        cursor
    'ownerid':int
    'xy':(int,int)
    'name':string
    'base type':string      # breast plate/ringmail/ancient armor?
    'quality': one of ['inferior','normal','superior','magic','set','rare',
        'unique','crafted']
    'category': one of ['weapon', 'armor', 'misc']
    'ethereal':boolean
    'condition'(int,int) # n, out of max
    'personalized':string
    'identified':boolean
    'sockets':int
    'properties':{'name':value,...}
    'dimensions': (int,int)
    'ilvl':int
        
    '''
    
#
# Modifiers:
#
    
def get(item):
    ''' Picks up the item, from the ground or an inventory.

    Item is on the ground:
REQUIRES: Inventory has enough room, item is valid.
EFFECTS: Item is placed in the inventory, provided no one gets to it first.

    Item is in inventory|stash|cube|belt|trade|mercenary|worn:
REQUIRES: Cursor is not holding an item, item is not gold. 
EFFECTS: Item is placed on the cursor.
TODO: you CAN pick up gold with the cursor, can't you?

    Effects of picking up other people's items, or non-items is undefined.
    Ground pickup not guaranteed due to competition from other players.
    '''	


def buy(item):
    ''' Buys an item from an NPC.

REQUIRES: Interacting with the NPC, have room in inventory, have enough gold,
    item is valid.
EFFECTS: Item is bought and worn or placed in inventory. Scrolls may stack into
books if books are present.
TODO: What about mass buy? (Shift+click or whatever.)

    '''

def drop(item):
    ''' Drops a held item or gold on the ground.

REQUIRES: Have an item on the cursor, or have enough gold. Item is valid.
EFFECTS: Drops item from cursor to ground. If item is gold, drops that amount
    of gold.
    '''
    
def place(dest, x=0, y=0):
    ''' Places a held item into an owned buffer.

REQUIRES: Nothing blocking the destination. 
EFFECTS: Puts the item on the cursor on the destination.

    Inventory slots are each treated as individual buffers, x and y can be
left as default for those.
    See TODO for a list of valid destination buffers.
    '''


def swap(item):
    ''' Swaps item with item on cursor.

REQUIRES: Item is worn or in a player-owned buffer, room exists for the item
    on the cursor.
EFFECTS: Item is put on the cursor, and what was on the cursor takes items'
    place.
    '''
    
def deposit():
    ''' Deposit all gold on person into stash.

REQUIRES: Interacting with the stash?
EFFECTS: Deposits as much gold as possible into your stash.
TODO: Confirm requires.
    '''

def getcorpse(target):
    ''' Loot a corpse (probably yours).

ARGUMENTS: TODO
REQUIRES: There's enough room to pick everything up off the course. Corpse in
    range.
CAUTION: Strength glitching can have a range of effects, from:
    -unable to pick up corpse in one go, to
    -unable to pick up corpse on a certain weapon switch, to
    -unable to pick up corpse at all. Beware.
    Also, let's re-iterate the requirement by pointing out that accidentally
    picking up an item while not geared will also result in a partial corpse
    pickup.
EFFECTS: Grabs everything off the corpse... If there's room.
    '''
	
