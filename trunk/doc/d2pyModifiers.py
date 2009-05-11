#---------------------80 characters long---------------------------------------#
#
#   General notes:
#
''' General API goals:
Minimalistic: require as little code to implement as possible.
General: there should be many possible ways to implement it.
Sufficient: almost any kind of bot should be writeable with this.

    Resulting problems:
Not total: unsatisfied requirements may cause Interesting results. This is
    necessary to conform to the minimalism goal.
Very general: one function returns all possible items, for example. This
    is also due to minimalism. 
    
    Notes:
Latency may delay effects on all modifier actions.
Parameters are required to be valid. Some requirements (max string length
    and allowed characters in particular) may be missing: use common sense.
Functions DO NOT BLOCK, return 'instantly' without confirmation of success.
    Particularly bad failure (logon, conn drop) may however result in
    exceptions.

    Formatting:
Lower case function names.
Capitalize first letter of sentence, end with .
ARGUMENTS/EFFECTS/etc. allcaps.
Variable names are all lower case, even if at start of sentence.
Example:
def func(alpha,beta):
    '"' Short function description.

ARGUMENTS: int,string
REQUIREMENTS: alpha must be a prime number.
EFFECTS: Sentences start with capital letters.
    '"'
'''


##
## MODIFIERS, TL;DR VERSION:
## 
# Startup:
def startup.startclient(path):
def startup.connect2bnet(realm, classic, xpac):
# Client started:
def startup.login(account, password):
# Logged in:
def startup.selectcharacter(name):
def channel.join(name): 
def channel.chat(msg):
def game.make(name):
def game.join(name):
# Item modifiers
def items.get(item):
def items.buy(item):
def items.drop(item):
def items.place(dest, x=0, y=0):
def items.swap(item):
def items.deposit():
def items.getcorpse(target):
# Instant
def comms.chat(message):
# Player relations
def comms.setstatus(player,status):
# Movement
def movement.run(x,y)  
def movement.run(target)
def movement.enter(portal)
def movement.waypoint(waypoint, dest)
# Spells
def spells.spell(right, spell):
def spells.cast(right, target):
def spells.cast(right, x, y):
def spells.weaponswitch():
# Interaction
def interactions.interact(target, goal="default"):
def interactions.stopinteraction():


#
#   MODIFIERS:
#

# Startup:
    
# Client started:

    
# Logged in:



#
# In game:
# REQUIRES: In game.
#

# Item modifiers

# Instant

# Movement

# Spells

# Interaction



