"""This file describes the heroic adventurer Sota.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.4"

name = "Sota"
player_name = "Alex"

# Be sure to list Primary class first
classes = ['Wizard']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [7]  # ex: [10] or [3, 2]
subclasses = ["School of Conjuration"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Hermit"
race = "Goliath"
alignment = "Lawful good"

xp = 0
hp_max = 27
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 19
dexterity = 13
constitution = 11
intelligence = 15  # +2 from Sling of Intelligence
wisdom = 10
charisma = 8

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('arcana', 'history', 'medicine', 'religion', 'athletics')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ()

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Sylvan"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ["Sling", "Dagger"]  # Example: ('shortsword', 'longsword')
magic_items = ["Oil of Sharpness", "Bracers of Defense",
               "Orb of Time"]  # Example: ('ring of protection',)
armor = "None"  # Eg "leather armor"
shield = "None"  # Eg "shield"

equipment = """Sling of Intelligence (+2 to INT). Amulet. Weaver's Tools. Broken Pouch. Hide Armor"""

attacks_and_spellcasting = """"""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
# 4 cantrips
# 7 spells
spells_prepared = ('blade ward', 'minor illusion', 'mending', 'fire bolt',  # 4 cantrips
                   'fog cloud', 'mage armor', 'magic missile',  # 6 spells @ 5th
                   'magic weapon', 'gust of wind', 'levitate',
                   'haste', 'magic circle')  # Todo: Learn some spells

# Which spells have not been prepared
# 6 1st level total
# 8 others total
__spells_unprepared = ('witch bolt', 'sleep', 'detect magic',  # 6 1st level
                       'suggestion', 'phantasmal force',    # 14 total
                       'protection from energy', 'stinking cloud',
                       'remove curse')

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ()  # Ex: ('ape', 'wolf', 'ankylosaurus')

# Backstory
# Describe your backstory here
personality_traits = """There is not limit to what the human body can do, out to prove myself"""

ideals = """dedication"""

bonds = """masters of thier art"""

flaws = """stubborn

Has no hands
"""

features_and_traits = """
TODO: Two new spells (level 4 spells available)
"""
