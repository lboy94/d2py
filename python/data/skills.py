'''Master lists of strings.

    Used for conversion between human-readable strings, and the numbers D2
actually uses. Thus, ORDER IS CRITICAL AND MAY NOT BE CHANGED!
    Some of these may later get converted to dictionaries, holding extra data
(act, aura skill, player/monster skill, etc) if it turns out to be necessary
or useful: keeping it simple is first priority however.
'''

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
    # Druid auras
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

effects = ["None", "Freeze", "Poison", "Resistfire", "Resistcold", "Resistlight", 
"Resistmagic", "Playerbody", "Resistall", "Amplifydamage", "Frozenarmor", 
"Cold", "Inferno", "Blaze", "Bonearmor", "Concentrate", "Enchant", 
"Innersight", "Skill Move", "Weaken", "Chillingarmor", "Stunned", "Spiderlay", 
"Dimvision", "Slowed", "Fetishaura", "Shout", "Taunt", "Conviction", 
"Convicted", "Energyshield", "Venomclaws", "Battleorders", "Might", "Prayer", 
"Holyfire", "Thorns", "Defiance", "Thunderstorm", "Lightningbolt", 
"Blessedaim", "Stamina", "Concentration", "Holywind", "Holywindcold", 
"Cleansing", "Holyshock", "Sanctuary", "Meditation", "Fanaticism", 
"Redemption", "Battlecommand", "Preventheal", "Conversion", "Uninterruptable", 
"Ironmaiden", "Terror", "Attract", "Lifetap", "Confuse", "Decrepify", 
"Lowerresist", "Openwounds", "Dopplezon", "Criticalstrike", "Dodge", "Avoid", 
"Penetrate", "Evade", "Pierce", "Warmth", "Firemastery", "Lightningmastery", 
"Coldmastery", "Swordmastery", "Axemastery", "Macemastery", "Polearmmastery", 
"Throwingmastery", "Spearmastery", "Increasedstamina", "Ironskin", 
"Increasedspeed", "Naturalresistance", "Fingermagecurse", "Nomanaregen", 
"Justhit", "Slowmissiles", "Shiverarmor", "Battlecry", "Blue", "Red", 
"Death Delay", "Valkyrie", "Frenzy", "Berserk", "Revive", "Itemfullset", 
"Sourceunit", "Redeemed", "Healthpot", "Holyshield", "Just Portaled", 
"Monfrenzy", "Corpse Nodraw", "Alignment", "Manapot", "Shatter", "Sync Warped", 
"Conversion Save", "Pregnant", "111", "Rabies", "Defense Curse", "Blood Mana", 
"Burning", "Dragonflight", "Maul", "Corpse Noselect", "Shadowwarrior", 
"Feralrage", "Skilldelay", "Progressive Damage", "Progressive Steal", 
"Progressive Other", "Progressive Fire", "Progressive Cold", 
"Progressive Lightning", "Shrine Armor", "Shrine Combat", 
"Shrine Resist Lightning", "Shrine Resist Fire", "Shrine Resist Cold", 
"Shrine Resist Poison", "Shrine Skill", "Shrine Mana Regen", "Shrine Stamina", 
"Shrine Experience", "Fenris Rage", "Wolf", "Bear", "Bloodlust", "Changeclass", 
"Attached", "Hurricane", "Armageddon", "Invis", "Barbs", "Wolverine", 
"Oaksage", "Vine Beast", "Cyclonearmor", "Clawmastery", "Cloak Of Shadows", 
"Recycled", "Weaponblock", "Cloaked", "Quickness", "Bladeshield", "Fade"]

## Pack list into 80-char lines.
#l=0;
#for e in effects:
#    elen = len(e)+4
#    if (l+elen)>80:
#        l=0; print("")
#    print('"'+e+'", ', end='')
#    l += elen
