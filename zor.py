"""This file describes the heroic adventurer Zor Daar.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.2"

name = "Zor Daar"
player_name = "Harshil"

# Be sure to list Primary class first
classes = ['Paladin']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [7]  # ex: [10] or [3, 2]
subclasses = ["Oath of Zor"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Soldier"
race = "Human"
alignment = "Chaotic Good"

xp = 0
hp_max = 54
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 16
dexterity = 12
constitution = 13
intelligence = 12
wisdom = 9
charisma = 14

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('athletics', 'intimidation', 'persuasion', 'religion')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = []

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = []

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ('Great-Weapon Fighting',)

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()
_proficiencies_text = ()

# Proficiencies and languages
languages = """Common, [Choose one]"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 110
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ["Flame Tongue", "War pick", "Javelin"]  # Example: ('shortsword', 'longsword')
magic_items = ["Flame Tongue", "Coins of Communication"]  # Example: ('ring of protection',)
armor = "Plate Mail"  # Eg "light leather armor"
shield = "None"  # Eg "shield"

equipment = """Explorer's pack. 3 small shards of glass. 5 Javelins"""

attacks_and_spellcasting = """5 Javelins"""

# List of known spells
# Example: spells = ('magic missile', 'mage armor')
spells = ("Bless", "Detect Poison and Disease")

# Which spells have been prepared (not including cantrips)
spells_prepared = ("Bless", "Detect Poison and Disease")

# Backstory
# Describe your backstory here
personality_traits = """
I think I am a god.

I am inflexible
"""

ideals = """
"""

bonds = """
"""

flaws = """
"""

features_and_traits = """
5 followers
"""
