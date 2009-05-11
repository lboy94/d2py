def npc(type,position,hp,id,dead,hostile):
    n = {
        'type':type,
        'position':position,
        'hp':hp,
        'id':id,
        'dead':dead,
        'hostile':hostile
        }
    return n

from random import choice,randint

#building list of random npcs
global npclist
#npclist = [npc(choice(['Fallen', 'Shaman', 'Skeleton']),
#        (randint(0,64000),randint(0,64000)),
#        1.0,
#        randint(0,9999),
#        choice([True,False]),
#        True) for x in range(0,100000)]

def closest(a,b):
    x,y = (32000,32000)
    i,j = a['position']
    arange = (x-i)**2 + (y-j)**2
    i,j = b['position']
    brange = (x-i)**2 + (y-j)**2
    if (arange>brange): return b
    else: return a

def findnearest():
    #reducing said list by distance
    from functools import reduce
    ret = reduce(closest,[x for x in npclist if not x['dead']])
    #print(ret)

def findmyitems():
    #reducing said list by distance
    ret = [x for x in itemlist if x in ['inventory', 'potion belt', 'cube']]
    #print(ret)
    

global itemlist
itemlist = [{'location':choice(['inventory', 'potion belt', 'cube',
    'stash', 'my trade', 'amulet', 'body', 'right primary', 'left primary',
                                ])} for x in range(1000)]
from timeit import Timer

t = Timer(stmt=findmyitems, setup='gc.enable()')

print(t.timeit(number=1))

# This iterator idea... Is fast enough. Worry about optimizing pickit lookup,
#   maybe. But NPC/object lookup, never.e

