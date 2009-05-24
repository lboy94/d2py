'''Master lists of strings.

    Used for conversion between human-readable strings, and the numbers D2
actually uses. Thus, ORDER IS CRITICAL AND MAY NOT BE CHANGED!
    Some of these may later get converted to dictionaries, holding extra data
(act, aura skill, player/monster skill, etc) if it turns out to be necessary
or useful: keeping it simple is first priority however.
'''

quality = ["None", "Inferior", "Normal", "Superior", "Magic", "Set", "Rare",
           "Unique", "Crafted"]

# Look for a way to merge locations+equipped?

locations = ["Unspecified", "Equipped", "Belt", "Ground", "Cursor", "Unknown",
             "Socketed"]

equipped = ["None", "Helm", "Amulet", "Armor", "Right Hand", "Left Hand",
            "Right Ring", "Left Ring", "Belt", "Boots", "Gloves",
            "Right Switch", "Left Switch"]


# Someone (ejact or binrapt?) once told me these were wrong but I didn't follow
# up. Will need to double check.
#  'Rings' and 'Class Specific' being entries but 'Bows' and whatnot not,
# suggests that the fix is as simple as removing 'rings' and 'class specific'.
#  Let's hope it is.
uniques = ["The Gnasher", "Deathspade", "Bladebone", "Mindrend", "Rakescar",
"Fechmars Axe", "Goreshovel", "The Chieftan", "Brainhew", "The Humongous",
"Iros Torch", "Maelstrom", "Gravenspine", "UmesLament", "Felloak",
"Knell Striker", "Rusthandle", "Stormeye", "Stoutnail", "Crushflange",
"Bloodrise", "The Generals Tan Do Li Ga", "Ironstone", "Bonesob", "Steeldriver",
"Rixots Keen", "Blood Crescent", "Krintizs Skewer", "Gleamscythe",
"azurewrath1", # heh
"Griswolds Edge", "Hellplague", "Culwens Point", "Shadowfang", "Soulflay",
"Kinemils Awl", "Blacktongue", "Ripsaw", "The Patriarch", "Gull",
"The Diggler (gigity-giggity!)", "The Jade Tan Do", "Irices Shard",
"The Dragon Chang", "Razortine", "Bloodthief", "Lance of Yaggai",
"The Tannr Gorerod", "Dimoaks Hew", "Steelgoad", "Soul Harvest",
"The Battlebranch", "Woestave", "The Grim Reaper", "Bane Ash", "Serpent Lord",
"Lazarus Spire", "The Salamander", "The Iron Jang Bong", "Pluckeye",
"Witherstring", "Rimeraven", "Piercerib", "Pullspite", "Wizendraw", "Hellclap",
"Blastbark", "Leadcrow", "Ichorsting", "Hellcast", "Doomspittle", "War Bonnet",
"Tarnhelm", "Coif of Glory", "Duskdeep", "Wormskull", "Howltusk",
"Undead Crown", "The Face of Horror", "Greyform", "Blinkbats Form",
"The Centurion", "Twitchthroe", "Darkglow", "Hawkmail", "Sparking Mail",
"Venomsward", "Iceblink", "Boneflesh", "Rockfleece", "Rattlecage", "Goldskin",
"Victors Silk", "Heavenly Garb", "Pelta Lunata", "Umbral Disk", "Stormguild",
"Wall of the Eyeless", "Swordback Hold", "Steelclash", "Bverrit Keep",
"The Ward", "The Hand of Broc", "Bloodfist", "Chance Guards", "Magefist",
"Frostburn", "Hotspur", "Gorefoot", "Treadsof Cthon", "Goblin Toe",
"Tearhaunch", "Lenyms Cord", "Snakecord", "Nightsmoke", "Goldwrap",
"Bladebuckle", "Nokozan Relic", "The Eye of Etlich", "The Mahim Oak Curio",
"Nagelring", "ManaldHeal", "The Stone of Jordan", "Amulet of the Viper",
"Staff of Kings", "Horadric Staff", "Hell Forge Hammer", "Khalim Flail",
"Super Khalim Flail", "Coldkill", "Butchers Pupil", "Islestrike",
"Pompes Wrath", "Guardian Naga", "Warlords Trust", "Spellsteel", "Stormrider",
"Boneslayer Blade", "The Minataur", "Suicide Branch", "Carin Shard",
"Arm of King Leoric", "Blackhand Key", "Dark Clan Crusher", "Zakarums Hand",
"The Fetid Sprinkler", "Hand of Blessed Light", "Fleshrender",
"Sureshrill Frost", "Moonfall", "Baezils Vortex", "Earthshaker",
"Bloodtree Stump", "TheGavelof Pain", "Bloodletter", "Coldsteel Eye", "Hexfire",
"Blade of Ali Baba", "Ginthers Rift", "Headstriker", "Plague Bearer",
"The Atlantian", "Crainte Vomir", "Bing Sz Wang", "The Vile Husk", "Cloudcrack",
"Todesfaelle Flamme", "Swordguard", "Spineripper", "Heart Carver",
"Blackbogs Sharp", "Stormspike", "The Impaler", "Kelpie Snare",
"Soulfeast Tine", "Hone Sundan", "Spireof Honor", "The Meat Scraper",
"Blackleach Blade", "Athenas Wrath", "Pierre Tombale Couant", "Husoldal Evo",
"Grims Burning Dead", "Razorswitch", "Ribcracker", "Chromatic Ire", "Warpspear",
"Skullcollector", "Skystrike", "Riphook", "Kuko Shakaku", "Endlesshail",
"Whichwild String", "Cliffkiller", "Magewrath", "Godstrike Arch",
"Langer Briser", "Pus Spiter", "Buriza Do Kyanon", "Demon Machine", "Armor",
"Peasent Crown", "Rockstopper", "Stealskull", "Darksight Helm", "Valkiry Wing",
"Crownof Thieves", "Blackhorns Face", "Vampiregaze", "The Spirit Shroud",
"Skin of the Vipermagi", "Skin of the Flayed One", "Ironpelt", "Spiritforge",
"Crow Caw", "Shaftstop", "Duriels Shell", "Skullders Ire", "Guardian Angel",
"Toothrow", "Atmas Wail", "Black Hades", "Corpsemourn", "Que Hegans Wisdon",
"Visceratuant", "Mosers Blessed Circle", "Stormchaser", "Tiamats Rebuke",
"Kerkes Sanctuary", "Radimants Sphere", "Lidless Wall", "Lance Guard",
"Venom Grip", "Gravepalm", "Ghoulhide", "Lavagout", "Hellmouth",
"Infernostride", "Waterwalk", "Silkweave", "Wartraveler", "Gorerider",
"String of Ears", "Razortail", "Gloomstrap", "Snowclash", "Thudergods Vigor",
"Elite Uniques", "Harlequin Crest", "Veil of Steel", "The Gladiators Bane",
"Arkaines Valor", "Blackoak Shield", "Stormshield", "Hellslayer",
"Messerschmidts Reaver", "Baranars Star", "Schaefers Hammer",
"The Cranium Basher", "Lightsabre", "Doombringer", "The Grandfather",
"Wizardspike", "Constricting Ring", "Stormspire", "Eaglehorn", "Windforce",
"Rings", # wtf, should this be here?
"Bul Kathos Wedding Band", "The Cats Eye", "The Rising Sun", "Crescent Moon",
"Maras Kaleidoscope", "Atmas Scarab", "Dwarf Star", "Raven Frost",
"Highlords Wrath", "Saracens Chance",
"Class Specific", # crap is this supposed to be here?!
"Arreats Face", "Homunculus", "Titans Revenge", "Lycanders Aim",
"Lycanders Flank", "The Oculus", "Herald of Zakarum",
"Bartucs Cutthroat", "Jalals Mane", "The Scalper", "Bloodmoon", "Djinnslayer",
"Deathbit", "Warshrike", "Gutsiphon", "Razoredge", "Gore Ripper", "Demonlimb",
"Steelshade", "Tomb Reaver", "Deathss Web", "Natures Peace", "Azurewrath",
"Seraphs Hymn", "Zakarums Salvation", "Fleshripper", "Odium",
"Horizons Tornado", "Stone Crusher", "Jadetalon", "Shadowdancer", "Cerebus",
"Tyraels Might", "Souldrain", "Runemaster", "Deathcleaver",
"Executioners Justice", "Stoneraven", "Leviathan", "Larzuks Champion",
"Wisp", "Gargoyles Bite", "Lacerator", "Mang Songs Lesson", "Viperfork",
"Ethereal Edge", "Demonhorns Edge", "TheReapers Toll", "Spiritkeeper",
"Hellrack", "Alma Negra", "Darkforge Spawn", "Widowmaker", "Bloodravens Charge",
"Ghostflame", "Shadowkiller", "Gimmershred", "Griffons Eye", "Windhammer",
"Thunderstroke", "Giantmaimer", "Demons Arch", "Boneflame", "Steelpillar",
"Nightwings Veil", "Crown of Ages", "Andariels Visage", "Darkfear",
"Dragonscale", "Steel Carapice", "Medusas Gaze", "Ravenlore", "Boneshade",
"Nethercrow", "Flamebellow", "Fathom", "Wolfhowl", "Spirit Ward",
"Kiras Guardian", "Ormus Robes", "Gheeds Fortune", "Stormlash",
"Halaberds Reign", "Warrivs Warder", "Spike Thorn", "Draculs Grasp",
"Frostwind", "Templars Might", "Eschutastemper", "Firelizards Talons",
"Sandstorm Trek", "Marrowwalk", "Heavens Light", "Mermans Speed",
"Arachnid Mesh", "Nosferatus Coil", "Metalgrid", "Verdugos Hearty Cord",
"Sigurds Staunch", "Carrion Wind", "Giantskull", "Ironward", "Annihilus",
"Ariocs Needle", "Cranebeak", "Nords Tenderizer", "Earthshifter",
"Wraithflight", "Bonehew", "Ondals Wisdom", "TheReedeemer", "Headhunters Glory",
"Steelrend", "Lightning Facet (Death)", "Cold Facet (Death)",
"Fire Facet (Death)", "Poison Facet (Death)", "Lightning Facet (Level)",
"Cold Facet (Level)", "Fire Facet (Level)", "Poison Facet (Level)",
"Hellfire Torch"
]

runewords = ["Invalid", "Ancients Pledge", "Armageddon", "Authority", "Beast",
"Beauty", "Black", "Blood", "Bone", "Bramble", "Brand", "Breath of the Dying",
"Broken Promise", "Call to Arms", "Chains of Honor", "Chance", "Chaos",
"Crescent Moon", "Darkness", "Daylight", "Death", "Deception", "Delirium",
"Desire", "Despair", "Destruction", "Doom", "Dragon", "Dread", "Dream",
"Duress", "Edge", "Elation", "Enigma", "Enlightenment", "Envy", "Eternity",
"Exile", "Faith", "Famine", "Flame", "Fortitude", "Fortune", "Friendship",
"Fury", "Gloom", "Glory", "Grief", "Hand of Justice", "Harmony", "Hatred",
"Heart of the Oak", "Heavens Will", "Holy Tears", "Holy Thunder", "Honor",
"Revenge", "Humility", "Hunger", "Ice", "Infinity", "Innocence", "Insight",
"Jealousy", "Judgement", "Kings Grace", "Kingslayer", "Knights Vigil",
"Knowledge", "Last Wish", "Law", "Lawbringer", "Leaf", "Lightning", "Lionheart",
"Lore", "Love", "Loyalty", "Lust", "Madness",
"Runeword80",   # Runeword80 doesn't exist!? Not defined in tbl either...
"Malice", "Melody", "Memory", "Mist", "Morning", "Mystery", "Myth", "Nadir",
"Natures Kingdom", "Night", "Oath", "Obedience", "Oblivion", "Obsession",
"Passion", "Patience", "Pattern", "Peace", "Voice of Reason", "Penitence",
"Peril", "Pestilence", "Phoenix", "Piety", "Pillar of Faith", "Plague",
"Praise", "Prayer", "Pride", "Principle", "Prowess In Battle", "Prudence",
"Punishment", "Purity", "Question", "Radiance", "Rain", "Reason", "Red",
"Rhyme", "Rift", "Sanctuary", "Serendipity", "Shadow", "Shadow of Doubt",
"Silence", "Sirens Song", "Smoke", "Sorrow", "Spirit", "Splendor", "Starlight",
"Stealth", "Steel", "Still Water", "Sting", "Stone", "Storm", "Strength",
"Tempest", "Temptation", "Terror", "Thirst", "Thought", "Thunder", "Time",
"Tradition", "Treachery", "Trust", "Truth", "Unbending Will", "Valor",
"Vengeance", "Venom", "Victory", "Voice", "Void", "War", "Water", "Wealth",
"Whisper", "White", "Wind", "Wings of Hope", "Wisdom", "Woe", "Wonder", "Wrath",
"Youth", "Zephyr", "Unknown"] # Interesting how these are alphabetic, except
                              # for the "Unknown" at the end :[
                              
sets = ["Civerbs Ward", "Civerbs Icon", "Civerbs Cudgel", "Hsarus Iron Heel",
"Hsarus Iron Fist", "Hsarus Iron Stay", "Cleglaws Tooth", "Cleglaws Claw",
"Cleglaws Pincers", "Irathas Collar", "Irathas Cuff", "Irathas Coil",
"Irathas Cord", "Isenharts Lightbrand", "Isenharts Parry", "Isenharts Case",
"Isenharts Horns", "Vidalas Barb", "Vidalas Fetlock", "Vidalas Ambush",
"Vidalas Snare", "Milabregas Orb", "Milabregas Rod", "Milabregas Diadem",
"Milabregas Robe", "Cathans Rule", "Cathans Mesh", "Cathans Visage",
"Cathans Sigil", "Cathans Seal", "Tancreds Crowbill", "Tancreds Spine",
"Tancreds Hobnails", "Tancreds Weird", "Tancreds Skull", "Sigons Gage",
"Sigons Visor", "Sigons Shelter", "Sigons Sabot", "Sigons Wrap",
"Sigons Guard", "Infernal Cranium", "Infernal Torch", "Infernal Sign",
"Berserkers Headgear", "Berserkers Hauberk", "Berserkers Hatchet",
"Deaths Hand", "Deaths Guard", "Deaths Touch", "Angelic Sickle",
"Angelic Mantle", "Angelic Halo", "Angelic Wings", "Arctic Horn", "Arctic Furs",
"Arctic Binding", "Arctic Mitts", "Arcannas Sign", "Arcannas Deathwand",
"Arcannas Head", "Arcannas Flesh", "Natalyas Totem", "Natalyas Mark",
"Natalyas Shadow", "Natalyas Soul", "Aldurs Stony Gaze", "Aldurs Deception",
"Aldurs Gauntlet", "Aldurs Advance", "Immortal Kings Will",
"Immortal Kings Soul Cage", "Immortal Kings Detail", "Immortal Kings Forge",
"Immortal Kings Pillar", "Immortal Kings Stone Crusher",
"Tal Rashas Fire Spun Cloth", "Tal Rashas Adjudication",
"Tal Rashas Lidless Eye", "Tal Rashas Howling Wind",
"Tal Rashas Horadric Crest", "Griswolds Valor", "Griswolds Heart",
"Griswolds Redemption", "Griswolds Honor", "Trang Ouls Guise",
"Trang Ouls Scales", "Trang Ouls Wing", "Trang Ouls Claws", "Trang Ouls Girth",
"Mavinas True Sight", "Mavinas Embrace", "Mavinas Icy Clutch", "Mavinas Tenet",
"Mavinas Caster", "Telling of Beads", "Laying of Hands", "Rite of Passage",
"Spiritual Custodian", "Credendum", "Dangoons Teaching", "Heavens Taebaek",
"Haemosus Adament", "Ondals Almighty", "Guillaumes Face", "Wilhelms Pride",
"Magnus Skin", "Wihtstans Guard", "Hwanins Splendor", "Hwanins Refuge",
"Hwanins Seal", "Hwanins Justice", "Sazabis Cobalt Redeemer",
"Sazabis Ghost Liberator", "Sazabis Mental Sheath", "Bul Kathos Sacred Charge",
"Bul Kathos Tribal Guardian", "Cow Kings Horns", "Cow Kings Hide",
"Cow Kings Hoofs", "Najs Puzzler", "Najs Light Plate", "Najs Circlet",
"Sanders Paragon", "Sanders Riprap", "Sanders Taboo", "Sanders Superstition"
]


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
