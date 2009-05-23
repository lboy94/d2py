'''Master lists of strings.

    Used for conversion between human-readable strings, and the numbers D2
actually uses. Thus, ORDER IS CRITICAL AND MAY NOT BE CHANGED!
    Some of these may later get converted to dictionaries, holding extra data
(act, aura skill, player/monster skill, etc) if it turns out to be necessary
or useful: keeping it simple is first priority however.
'''

levels = [
    "Unknown",
    # Act 1, cow level counts as Act 1
    "Rogue Encampment", "Blood Moor", "Cold Plains", "Stony Field", "Dark Wood",
    "Black Marsh", "Tamoe Highland", "Den Of Evil", "Cave Level 1",
    "Underground Passage Level 1", "Hole Level 1", "Pit Level 1",
    "Cave Level 2", "Underground Passage Level 2", "Holy Level 2",
    "Pit Level 2", "Burial Grounds", "Crypt", "Mausoleum", "Forgotten Tower",
    "Tower Cellar Level 1", "Tower Cellar Level 2", "Tower Cellar Level 3",
    "Tower Cellar Level 4", "Tower Cellar Level 5", "Monastery Gate",
    "Outer Cloister", "Barracks", "Jail Level 1", "Jail Level 2",
    "Jail Level 3", "Inner Cloister", "Inner Cloister 2", "Catacombs Level 1",
    "Catacombs Level 2", "Catacombs Level 3", "Catacombs Level 4", "Tristram",
    "The Secret Cow Level",
    # Act 2
    "Lut Gholein", "Rocky Waste", "Dry Hills", "Far Oasis", "Lost City",
    "Valley Of Snakes", "Canyon Of The Magi", "Sewers Level 1",
    "Sewers Level 2", "Sewers Level 3", "Harem Level 1", "Harem Level 2",
    "Palace Cellar Level 1", "Palace Cellar Level 2", "Palace Cellar Level 3",
    "Stony Tomb Level 1", "Halls Of The Dead Level 1",
    "Halls Of The Dead Level 2", "Claw Viper Temple Level 1",
    "Stony Tomb Level 2", "Halls Of The Dead Level 3",
    "Claw Viper Temple Level 2", "Maggot Lair Level 1", "Maggot Lair Level 2",
    "Maggot Lair Level 3", "Ancient Tunnels", "Tal Rashas Tomb 1",
    "Tal Rashas Tomb 2", "Tal Rashas Tomb 3", "Tal Rashas Tomb 4",
    "Tal Rashas Tomb 5", "Tal Rashas Tomb 6", "Tal Rashas Tomb 7",
    "Tal Rashas Chamber", "Arcane Sanctuary",
    # Act 3
    "Kurast Docks", "Spider Forest", "Great Marsh", "Flayer Jungle",
    "Lower Kurast", "Kurast Bazaar", "Upper Kurast", "Kurast Causeway",
    "Travincal", "Archnid Lair", "Spider Cavern", "Swampy Pit Level 1",
    "Swampy Pit Level 2", "Flayer Dungeon Level 1", "Flayer Dungeon Level 2",
    "Swampy Pit Level 3", "Flayer Dungeon Level 3", "Sewers Level 1",
    "Sewers Level 2", "Ruined Temple", "Disused Fane", "Forgotten Reliquary",
    "Forgotten Temple", "Ruined Fane", "Disused Reliquary",
    "Durance Of Hate Level 1", "Durance Of Hate Level 2",
    "Durance Of Hate Level 3",
    # Act 4
    "The Pandemonium Fortress", "Outer Steppes", "Plains Of Despair",
    "City Of The Damned", "River Of Flame", "The Chaos Sanctuary",
    # Act 5, Uber-tristram counts as Act 5
    "Harrogath", "The Bloody Foothills", "Frigid Highlands", "Arreat Plateau",
    "Crystalline Passage", "Frozen River", "Glacial Trail", "Drifter Cavern",
    "Frozen Tundra", "The Ancients Way", "Icy Cellar",
    "Arreat Summit", "Nihlathaks Temple", "Halls Of Anguish", "Halls Of Pain",
    "Halls Of Vaught", "Abaddon", "Pit Of Acheron", "Infernal Pit",
    "Worldstone Keep Level 1", "Worldstone Keep Level 2",
    "Worldstone Keep Level 3", "Throne Of Destruction", "Worldstone Keep",
    "Matrons Den", "Forgotten Sands", "Furnace Of Pain", "Uber Tristram"
    ]

skills = [
    # General
    "Attack", "Kick", "Throw", "Unsummon", "Left Hand Throw", "Left Hand Swing",
    # Amazon - decoy's internal name was Dopplezon, lol
    "Magic Arrow", "Fire Arrow", "Inner Sight", "Critical Strike", "Jab",
    "Cold Arrow", "Multiple Shot", "Dodge", "Power Strike", "Poison Javelin",
    "Exploding Arrow", "Slow Missiles", "Avoid", "Impale", "Lightning Bolt",
    "Ice Arrow", "Guided Arrow", "Penetrate", "Charged Strike",
    "Plague Javelin", "Strafe", "Immolation Arrow", "Decoy", "Evade", "Fend",
    "Freezing Arrow", "Valkyrie", "Pierce", "Lightning Strike",
    "Lightning Fury",
    # Sorceress
    "Fire Bolt", "Warmth", "Charged Bolt", "Ice Bolt", "Frozen Armor",
    "Inferno", "Static Field", "Telekinesis", "Frost Nova", "Ice Blast",
    "Blaze", "Fire Ball", "Nova", "Lightning", "Shiver Armor", "Fire Wall",
    "Enchant", "Chain Lightning", "Teleport", "Glacial Spike", "Meteor",
    "Thunder Storm", "Energy Shield", "Blizzard", "Chilling Armor",
    "Fire Mastery", "Hydra", "Lightning Mastery", "Frozen Orb", "Cold Mastery",
    # Necromancer
    "Amplify Damage", "Teeth", "Bone Armor", "Skeleton Mastery",
    "Raise Skeleton", "Dim Vision", "Weaken", "Poison Dagger",
    "Corpse Explosion", "Clay Golem", "Iron Maiden", "Terror", "Bone Wall",
    "Golem Mastery", "Raise Skeletal Mage", "Confuse", "Life Tap",
    "Poison Explosion", "Bone Spear", "Bloodgolem", "Attract", "Decrepify",
    "Bone Prison", "Summon Resist", "Iron Golem", "Lower Resist", "Poison Nova",
    "Bone Spirit", "Firegolem", "Revive",
    # Paladin
    "Sacrifice", "Smite", "Might", "Prayer", "Resist fire", "Holy bolt",
    "Holy fire", "Thorns", "Defiance", "Resist cold", "Zeal", "Charge",
    "Blessed aim", "Cleansing", "Resist lightning", "Vengeance",
    "Blessed  Hammer", "Concentration", "Holy freeze", "Vigor", "Conversion",
    "Holy  Shield", "Holy  Shock", "Sanctuary", "Meditation",
    "Fist  Of  Heavens", "Fanaticism", "Conviction", "Redemption", "Salvation",
    # Barbarian
    "Bash", "Sword Mastery", "Axe Mastery", "Mace Mastery", "Howl",
    "Find Potion", "Leap", "Double Swing", "Pole Arm Mastery",
    "Throwing Mastery", "Spear Mastery", "Taunt", "Shout", "Stun",
    "Double Throw", "Increased Stamina", "Find Item", "Leap Attack",
    "Concentrate", "Iron Skin", "Battle Cry", "Frenzy", "Increased Speed",
    "Battle Orders", "Grim Ward", "Whirlwind", "Berserk", "Natural Resistance",
    "War Cry", "Battle Command",
    # Monster, classic?
    "Fire Hit", "Unholybolt", "Skeletonraise", "Maggot Egg", "Shaman Fire",
    "Magott Up", "Magott Down", "Magott Lay", "Andrial Spray", "Jump",
    "Swarm Move", "Nest", "Quick Strike", "Vampirefireball", "Vampirefirewall",
    "Vampiremeteor", "Gargoyle Trap", "Spider Lay", "Vampire Heal",
    "Vampire Raise", "Sub Merge", "Fetish Aura", "Fetish Inferno",
    "Zakarum Heal", "Emerge", "Resurrect", "Bestow", "Missile Skill1",
    "Monster Teleport", "Prime Lightning", "Prime Bolt", "Prime Blaze",
    "Prime Firewall", "Prime Spike", "Prime Ice Nova", "Prime Poison Ball",
    "Prime Poison Nova", "Diablo Light", "Diablo Cold", "Diablo Fire",
    "Finger Mage Spider", "Diablo Firestorm", "Diablo Run", "Diablo Prison",
    "Poison Ball Trap", "Andy Poison Bolt", "Hireable Missile", "Desert Turret",
    "Arcane Tower", "Monster Blizzard", "Mosquito", "Cursedballtrapright",
    "Cursedballtrapleft", "Monster Frozen Armor", "Monster Bone Armor",
    "Monster Bone Spirit", "Monster Curse Cast", "Hell Meteor",
    "Regurgitator Eat", "Monster Frenzy", "Queen Death",
    # Scrolls and books: note how the two differ!
    "Scroll Of Identify", "Book Of Identify",
    "Scroll Of Townportal", "Book Of Townportal",
    # Druid
    "Raven", "Poison Creeper", "Wearwolf", "Shape Shifting", "Firestorm",
    "Oak Sage", "Summon Spirit Wolf", "Wearbear", "Molten Boulder",
    "Arctic Blast", "Cycle Of Life", # the life-eating vine?
    "Feral Rage", "Maul", "Fissure",
    "Cyclone Armor", "Heart Of Wolverine", "Summon Dire Wolf", "Rabies",
    "Fire Claws", "Twister", "Vines", # the mana-gaining vine?
    "Hunger", "Shock Wave", "Volcano",
    "Tornado", "Spirit Of Barbs", "Summon Grizzly", "Fury", "Armageddon",
    "Hurricane",
    # Assassin
    "Fire Blast", "Claw Mastery", "Psychic Hammer", "Tiger Strike",
    "Dragon Talon", "Shock Web", "Blade Sentinel", "Burst Of Speed",
    "Fists Of Fire", "Dragon Claw", "Charged Bolt Sentry", "Wake Of Fire",
    "Weapon Block", "Cloak Of Shadows", "Cobra Strike", "Blade Fury", "Fade",
    "Shadow Warrior", "Claws Of Thunder", "Dragon Tail", "Lightning Sentry",
    "Wake Of Inferno", "Mind Blast", "Blades Of Ice", "Dragon Flight",
    "Death Sentry", "Blade Shield", "Venom", "Shadow Master", "Phoenix Strike",
    "Wake Of Destruction Sentry", # <-- what the heck is this?
    # Mo' monsters, expansion?
    "Imp Inferno", "Imp Fireball", "Baal Taunt", "Baal Corpse Explode",
    "Baal Monster Spawn", # potentially useful, need spell event...
    "Catapult Charged Ball", "Catapult Spike Ball", "Suck Blood", "Cry Help",
    "Healing Vortex", "Teleport2", "Selfresurrect", "Vine Attack",
    "Overseer Whip",
    # Auras
    "Barbs Aura", "Wolverine Aura", "Oak Sage Aura",
    # More monster skills...
    "Imp Fire Missile", "Impregnate", "Siege Beast Stomp", "Minion Spawner",
    "Catapult Blizzard", "Catapult Plague", "Catapult Meteor", "Bolt Sentry",
    "Corpse Cycler", "Death Maul", "Defense Curse", "Blood Mana",# <- useful?
    "Inferno Sentry2", "Death Sentry2", "Sentry Lightning", "Fenris Rage",
    "Baal Tentacle", "Baal Nova", "Baal Inferno", "Baal Cold Missiles",
    "Mega Demon Inferno", "Evil Hut Spawner", "Countess Firewall", "Imp Bolt",
    "Horror Arctic Blast", "Death Sentry Lightning", "Vine Cycler",
    "Bear Smite", "Resurrect2", "Blood Lord Frenzy", "Baal Teleport",
    "Imp Teleport", "Baal Clone Teleport", "Zakarum Lightning",
    "Vampire Missile", "Mephisto Missile", # <- dodging this would be sweet
    "Doom Knight Missile", "Rogue Missile", "Hydra Missile",
    "Necromage Missile", "Monster Bow", "Monster Fire Arrow",
    "Monster Cold Arrow", "Monster Exploding Arrow", "Monster Freezing Arrow",
    "Monster Power Strike", "Succubus Bolt", "Mephisto Frost Nova",
    "Monster Ice Spear", "Shaman Ice", "Diablo Armageddon", "Delirium",
    "Nihlathak Corpse Explosion", "Serpent Charge", "Trap Nova",
    "Un Holy Bolt Ex", "Shaman Fire Ex", "Imp Fire Missile Ex"
    ]

classes = ["Amazon", "Sorceress", "Necromancer", "Paladin", "Barbarian",
           "Druid", "Assassin"]

# Using itemdata.py may be a good idea for the rest of these:

quality = ["None", "Inferior", "Normal", "Superior", "Magic", "Set", "Rare",
           "Unique", "Crafted"]

# Look for a way to merge locations+equipped?

locations = ["Unspecified", "Equipped", "Belt", "Ground", "Cursor", "Unknown",
             "Socketed"]

equipped = ["None", "Helm", "Amulet", "Armor", "Right Hand", "Left Hand",
            "Right Ring", "Left Ring", "Belt", "Boots", "Gloves",
            "Right Switch", "Left Switch"]

#                                                       shep called 5 tile?
#           0         1      2         3          4       5
#objectType ["Player", "NPC", "Object", "Missile", "Item", "Waypoint"]
# Will this be useful? ^ High chance of encapsulation inside C code.

# This will be useful in some form... May need to modify it though.
_CURRENTLY_NOT_USED_buffers = [
    "Belt", # comment said it was belt, but is it?
    "INVALID",
    "Inventory",
    "NotACube", # haven't seen this happen...
    "Their Trade",
    "5",
    "My Trade",
    "7",
    "Cube",
    "9",
    "Stash", 
    # following values are never actually seen
    # this section is here so on shop actions, you can add 11 to
    # the index and get shop-specific results (since this field
    # means different things depending on whether you're dealing
    # with player items or shop items)
    "0" ,
    "INVALID",
    "Armor Tab",
    "Armor Tab Extended",
    "Weapons Tab", 
    "Weapons Tab Extended",
    "2nd Weapons Tab",
    "2nd Weapons Tab Extended",
    "Misc Tab",
    "Misc Tab Extended"
    ]            


# Some code to re-format strings:
for s in levels:
    s2 = ''
    #for l in s:
    #    if l.isupper(): s2 += l.tolower()
    #    else: s2 += l
    s2 = s.lower()
    print('"'+s2+'",')
 






            
        
