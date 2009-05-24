'''Master lists of strings.

    Used for conversion between human-readable strings, and the numbers D2
actually uses. Thus, ORDER IS CRITICAL AND MAY NOT BE CHANGED!
    Some of these may later get converted to dictionaries, holding extra data
(act, aura skill, player/monster skill, etc) if it turns out to be necessary
or useful: keeping it simple is first priority however.
'''

# -1 may signify not being a superunique?
superuniques = ["Bishibosh", "Bonebreak", "Coldcrow", "Rakanishu", "Treehead WoodFist", 
"Griswold", "The Countess", "Pitspawn Fouldog", "Flamespike the Crawler", 
"Boneash", "Radament", "Bloodwitch the Wild", "Fangskin", "Beetleburst", 
"Leatherarm", "Coldworm the Burrower", "Fire Eye", "Dark Elder", 
"The Summoner", "Ancient Kaa the Soulless", "The Smith", 
"Web Mage the Burning", "Witch Doctor Endugu", "Stormtree", 
"Sarina the Battlemaid", "Icehawk Riftwing", "Ismail Vilehand", 
"Geleb Flamefinger", "Bremm Sparkfist", "Toorc Icefist", "Wyand Voidfinger", 
"Maffer Dragonhand", "Winged Death", "The Tormentor", "Taintbreeder", 
"Riftwrath the Cannibal", "Infector of Souls", "Lord De Seis", 
"Grand Vizier of Chaos", "The Cow King", "Corpsefire", "The Feature Creep", 
"Shenk the Overseer", "Talic", "Madawc", "Korlic", "Axe Dweller", 
"Bonesaw Breaker", "Dac Farren", "Megaflow Rectifer", "Eyeback Unleashed", 
"Threash Socket", "Pindleskin", "Snapchip Shatter", "Anodized Elite", 
"Vinvear Molech", "Sharp Tooth Sayer", "Magma Torquer", "Blaze Ripper", 
"Frozenstein", "Nihlathak", "Colenzo the Annihilator", "Achmel the Cursed", 
"Bartuc the Bloody", "Ventar the Unholy", "Lister the Tormentor"]

npcs = ["Skeleton", "Returned", "Bone Warrior", "Burning Dead", "Horror", "Zombie", 
"Hungry Dead", "Ghoul", "Drowned Carcass", "Plague Bearer", "Afflicted", 
"Tainted", "Misshappen", "Disfigured", "Damned", "Foul Crow", "BloodHawk", 
"Black Raptor", "Cloud Stalker", "Fallen", "Carver", "Devil Kin", "DarkOne", 
"Warped Fallen", "Brute", "Yeti", "Crusher", "Wailing Beast", 
"Gargantuan Beast", "Sand Raider", "Marauder", "Invader", "Infidel", 
"Assailant", "Unknown 34", "Unknown 35", "Unknown 36", "Unknown 37", "Ghost", 
"Wraith", "Specter", "Apparition", "Dark Shape", "Dark Hunter", "Vile Hunter", 
"Dark Stalker", "Black Rogue", "Flesh Hunter", "Dune Beast", "Rock Dweller", 
"Jungle Hunter", "Doom Ape", "Temple Guard", "Moon Clan", "Night Clan", 
"Blood Clan", "Hell Clan", "Death Clan", "Fallen Shamen", "Carver Shamen", 
"Devilkin Shamen", "Dark Shamen", "Warped Shamen", "Quill Rat", "Spike Fiend", 
"Thorn Beast", "Razor Spike", "Jungle Urchin", "Sand Maggot", "Rock Worm", 
"Devourer", "Giant Lamprey", "World Killer", "Tomb Viper", "Claw Viper", 
"Salamander", "Pit Viper", "Serpent Magus", "Sand Leaper", "Cave Leaper", 
"Tomb Creeper", "Tree Lurker", "Razor Pit Demon", "Huntress", "Saber Cat", 
"Night Tiger", "Hell Cat", "Itches", "Black Locusts", "Plague Bugs", 
"Hell Swarm", "Dung Soldier", "Sand Warrior", "Scarab", "Steel Weevil", 
"Albino Roach", "Dried Corpse", "Decayed", "Embalmed", "Preserved Dead", 
"Cadaver", "Hallow One", "Guardian", "Unraveler", "Horadrim Ancient", 
"Baal Subject Mummy", "Unknown 106", "Unknown 107", "Unknown 108", 
"Unknown 109", "Carrion Bird", "UndeadS cavenger", "Hell Buzzard", 
"Winged Nightmare", "Sucker", "Feeder", "Blood Hook", "Blood Wing", "Gloam", 
"Swamp Ghost", "Burning Soul", "Black Soul", "Arach", "Sand Fisher", 
"Poison Spinner", "Flame Spider", "Spider Magus", "Thorned Hulk", 
"Bramble Hulk", "Thrasher", "Spike Fist", "Ghoul Lord", "Night Lord", 
"Dark Lord", "Blood Lord", "Banished", "Desert Wing", "Fiend", "Gloom Bat", 
"Blood Diver", "Dark Familiar", "Rat Man", "Fetish", "Flayer", "Soul Killer", 
"Stygian Doll", "Deckard Cain", "Gheed", "Akara", "Unknown 149", "Kashya", 
"Unknown 151", "Unknown 152", "Unknown 153", "Charsi", "Warriv", "Andarial", 
"Unknown 157", "Unknown 158", "Unknown 159", "Dark Ranger", "Vile Archer", 
"Dark Archer", "Black Archer", "Flesh Archer", "Dark Spearwomen", 
"Vile Lancer", "Dark Lancer", "Black Lancer", "Flesh Lancer", 
"Skeleton Archer", "Returned Archer", "Bone Archer", "Burning Dead Archer", 
"Horror Archer", "Warriv", "Atma", "Drognan", "Fara", "Unknown 179", 
"Sand Maggot Young", "Rock Worm Young", "Devourer Young", 
"Giant Lamprey Young", "World Killer Yound", "Unknown 185", "Blunderbore", 
"Gorbelly", "Mauler", "Urdar", "Sand Maggot Egg", "Rock Worm Egg", 
"Devourer Egg", "Giant Lamprey Egg", "World Killer Egg", "Unknown 195", 
"Unknown 196", "Unknown 197", "Greiz", "Elzix", "Geglash", "Jerhyn", 
"Lysander", "Unknown 203", "Unknown 204", "Unknown 205", "Foul Crow Nest", 
"Blood Hawk Nest", "Black Vulture Nest", "Cloud Stalker Nest", "Meshif", 
"Duriel", "Unknown 212", "Unknown 213", "Unknown 214", "Unknown 215", 
"Unknown 216", "Unknown 217", "Unknown 218", "Unknown 219", "Unknown 220", 
"Unknown 221", "Unknown 222", "Unknown 223", "Unknown 224", "Unknown 225", 
"Unknown 226", "Maggot", "Mummy Generator", "Radament", "Unknown 230", 
"Unknown 231", "Unknown 232", "Unknown 233", "Flying Scimitar", "Zakarumite", 
"Faithful", "Zealot", "Sexton", "Cantor", "Heirophant", "Heirophant", 
"Mephesto", "Diablo", "Deckard Cain", "Deckard Cain", "Deckard Cain", 
"Swamp Dweller", "Bog Creature", "Slime Prince", "Summoner", "Tyrael", 
"Asheara", "Hratli", "Alkor", "Ormus", "Izual", "Halbu", "Water Watcher Limb", 
"River Stalker Limb", "Stygain Watcher Limb", "Water Watcher Head", 
"River Stalker Head", "Stygain Watcher Head", "Meshif", "Deckard Cain", "Navi", 
"Blood Raven", "Unknown 268", "Unknown 269", "Rogue Scout", "Unknown 271", 
"Unknown 272", "Gargoyle Trap", "Returned Mage", "Bone Mage", 
"Burning Dead Mage", "Horror Mage", "Rat Man Shamen", "Fetish Shamen", 
"Flayer Shamen", "Soul Killer Shamen", "Stygian Doll Shamen", "Larva", 
"Sand Maggot Queen", "Rock Worm Queen", "Devourer Queen", 
"Giant Lamprey Queen", "World Killer Queen", "Clay Golem", "Blood Golem", 
"Iron Golem", "Fire Golem", "Unknown 293", "Unknown 294", "Night Maraduer", 
"Unknown 296", "Natalya", "Flesh Spawner", "Stygian Hag", "Grotesque", 
"Flesh Beast", "Stygian Dog", "Grotesque Wyrm", "Groper", "Strangler", 
"Storm Caster", "Corpulent", "Corpse Spitter", "Maw Fiend", "Doom Knight", 
"Abyss Knight", "Oblivion Knight", "Quill Bear", "Spike Giant", "Thorn Brute", 
"Razor Beast", "Giant Urchin", "Unknown 318", "Unknown 319", "Unknown 320", 
"Unknown 321", "Unknown 322", "Unknown 323", "Unknown 324", "Unknown 325", 
"A Trap", "A Trap", "A Trap", "A Trap", "A Trap", "Kaelan", "Unknown 332", 
"Unknown 333", "Sucker Nest", "Feeder Nest", "Blood Hook Nest", 
"Blood Wing Nest", "Guard", "Unknown 339", "Unknown 340", "Unknown 341", 
"Unknown 342", "Unknown 343", "Unknown 344", "Council Member", 
"Council Member", "Council Member", "Turret", "Turret", "Turret", "Hydra", 
"Hydra", "Hydra", "A Trap", "Unknown 355", "Dopplezon", "Valkyrie", 
"Unknown 358", "Iron Wolf", "Balrog", "Pit Lord", "Venom Lord", 
"Necro Skeleton", "Necro Mage", "Griswold", "Compelling Orb", "Tyrael", 
"Young Diablo", "A Trap", "Unknown 370", "Lightning Spire", "Fire Tower", 
"Slinger", "Spear Cat", "Night Slinger", "Hell Slinger", "Unknown 377", 
"Unknown 378", "Returned Mage", "Bone Mage", "Baal Cold Mage", "Horror Mage", 
"Returned Mage", "Bone Mage", "Burning Dead Mage", "Horror Mage", 
"Returned Mage", "Bone Mage", "Burning Dead Mage", "Horror Mage", 
"Hell Bovine", "Unknown 392", "Unknown 393", "Spear Cat", "Night Slinger", 
"Rat Man", "Fetish", "Flayer", "Soul Killer", "Stygian Doll", "Unknown 401", 
"The Smith", "Traped Soul", "Traped Soul", "Jamella", "Izual", "Rat Man", 
"Malachai", "The Feature Creep", "Unknown 410", "Wake Of Destruction", 
"Charged Bolt Sentry", "Lightning Sentry", "Blade Creeper", "Invis Pet", 
"Inferno Sentry", "Death Sentry", "Shadow Warrior", "Shadow Master", 
"Druid Hawk", "Druid Spirit Wolf", "Druid Fenris", "Spirit Of Barbs", 
"Heart Of Wolverine", "Oak Sage", "Druid Plague Poppy", "Druid Cycle Of Life", 
"Vine Creature", "Druid Bear", "Eagle", "Wolf", "Bear", "Barricaded Door", 
"Barricaded Door", "Prison Door", "Barricaded Door", "Rot Walker", 
"Reanimate Horde", "Prowling Dead", "Unholy Corpse", "Defiled Warrior", 
"Siege Beast", "Crush Biest", "Blood Bringer", "Gore Bearer", "Deamon Steed", 
"Snow Yeti 1", "Snow Yeti 2", "Snow Yeti 3", "Snow Yeti 4", "Wolf Rider 1", 
"Wolf Rider 2", "Wolf Rider 3", "Minionexp", "Slayerexp", "Ice Boar", 
"Fire Boar", "Hell Spawn", "Ice Spawn", "Greater Hell Spawn", 
"Greater Ice Spawn", "Fanatic Minion", "Berserk Slayer", "Consumed Fire Boar", 
"Consumed Ice Boar", "Frenzied Hell Spawn", "Frenzied Ice Spawn", 
"Insane Hell Spawn", "Insane Ice Spawn", "Succubusexp", "Vile Temptress", 
"Stygian Harlot", "Hell Temptress", "Blood Temptress", "Dominus", "Vile Witch", 
"Stygian Fury", "Blood Witch", "Hell Witch", "Over Seer", "Lasher", 
"Over Lord", "Blood Boss", "Hell Whip", "Minion Spawner", 
"Minion Slayer Spawner", "Minion Ice/Fire Boar Spawner", 
"Minion Ice/Fire Boar Spawner", "Minion Ice/Hell Spawn Spawner", 
"Minion Ice/Fire Boar Spawner", "Minion Ice/Fire Boar Spawner", 
"Minion Ice/Hell Spawn Spawner", "Imp 1", "Imp 2", "Imp 3", "Imp 4", "Imp 5", 
"Catapults", "Catapulte", "Catapult Seige", "Catapult W", "Frozen Horror 1", 
"Frozen Horror 2", "Frozen Horror 3", "Frozen Horror 4", "Frozen Horror 5", 
"Blood Lord 1", "Blood Lord 2", "Blood Lord 3", "Blood Lord 4", "Blood Lord 5", 
"Larzuk", "Drehya", "Malah", "Nihlathak", "Qual-kehk", "Catapult Spotter S", 
"Catapult Spotter E", "Catapult Spotter Siege", "Catapult Spotter W", 
"Deckard Cain", "Tyrael", "Barbarian Fighter", "Barbarian Fighter", 
"Barricade Wall Right", "Barricade Wall Left", "Nihlathak", "Drehya", 
"Evil Hut", "Death Mauler 1", "Death Mauler 2", "Death Mauler 3", 
"Death Mauler 4", "Death Mauler 5", "POW", "Barbarian Fighter", 
"Barbarian Fighter", "Ancient Statue 1", "Ancient Statue 2", 
"Ancient Statue 3", "Ancient Barbarian 1", "Ancient Barbarian 2", 
"Ancient Barbarian 3", "Baal Throne", "Baal Crab", "Baal Taunt", 
"Putrid Defiler", "Putrid Defiler", "Putrid Defiler", "Putrid Defiler", 
"Putrid Defiler", "Pain Worm", "Pain Worm", "Pain Worm", "Pain Worm", 
"Pain Worm", "Bunny", "Council Member", "Venom Lord", "Baal Crab To Stairs", 
"Hireling", "Hireling", "Baal Tentacle", "Baal Tentacle", "Baal Tentacle", 
"Baal Tentacle", "Baal Tentacle", "Injured Barbarian", "Injured Barbarian", 
"Injured Barbarian", "Baal Crab Clone", "Baals Minion", "Baals Minion", 
"Baals Minion", "Worldstone Effect"]


## Pack list into 80-char lines.
#l=0;
#for e in superuniques:
#    elen = len(e)+4
#    if (l+elen)>80:
#        l=0; print("")
#    print('"'+e+'", ', end='')
#    l += elen