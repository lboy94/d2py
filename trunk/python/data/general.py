'''Master lists of strings.

    Used for conversion between human-readable strings, and the numbers D2
actually uses. Thus, ORDER IS CRITICAL AND MAY NOT BE CHANGED!
    Some of these may later get converted to dictionaries, holding extra data
(act, aura skill, player/monster skill, etc) if it turns out to be necessary
or useful: keeping it simple is first priority however.
'''

classes = ["Amazon", "Sorceress", "Necromancer", "Paladin", "Barbarian",
           "Druid", "Assassin"]
#                                                       shep called 5 tile?
#           0         1      2         3          4       5
objtype = ["Player", "NPC", "Object", "Missile", "Item", "Waypoint"]



# Some code to re-format strings:
#for s in levels:
#    s2 = ''
#    #for l in s:
#    #    if l.isupper(): s2 += l.tolower()
#    #    else: s2 += l
#    s2 = s.lower()
#    print('"'+s2+'",')
 






            
        
