"""This file describes the heroic adventurer Sota.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.2"

name = "Sota"
player_name = "Alex"

# Be sure to list Primary class first
classes = ['Monk', 'Fighter']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [1, 2]  # ex: [10] or [3, 2]
subclasses = ['', "Battle Master"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Hermit"
race = "Human"
alignment = "Chaotic good"

xp = 0
hp_max = 23
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 16
dexterity = 13
constitution = 12
intelligence = 11
wisdom = 20
charisma = 8

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('acrobatics', 'athletics', 'medicine', 'religion', 'stealth')

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
feature_choices = ('Dueling',)

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ('Heavy Punch',)
_proficiencies_text = ()

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
weapons = ["Unarmed", "Heavy Punch"]  # Example: ('shortsword', 'longsword')
magic_items = []  # Example: ('ring of protection',)
armor = "None"  # Eg "light leather armor"
shield = "None"  # Eg "shield"

equipment = """TODO: Describe your equipment from your Monk class and Hermit background."""

attacks_and_spellcasting = """TODO: Describe specifics for how your Monk attacks."""

# List of known spells
# Example: spells = ('magic missile', 'mage armor')
spells = ()

# Which spells have been prepared (not including cantrips)
spells_prepared = ()

# Backstory
# Describe your backstory here
personality_traits = """There is no limit to what the human body can do.
Out to prove myself.
"""

ideals = """Dedication
"""

bonds = """Masters of their art
"""

flaws = """Stubborn
"""

features_and_traits = """*Great Weapon Master (-5 attack, +10 damage)

*Second Wind

*Dueling +2

*Action Surge
"""
