"""This file describes the heroic adventurer Ma'caw.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.2"

name = "Ma'caw"
player_name = "Ashley"

# Be sure to list Primary class first
classes = ['Revised Ranger', "Fighter"]  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [3, 1]  # ex: [10] or [3, 2]
subclasses = ["Beast Conclave", None]  # ex: ['Necromacy'] or ['Thief', None]
background = "Outlander"
race = "Kenku"
alignment = "Neutral"

xp = 0
hp_max = 25
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 8
dexterity = 17
constitution = 10
intelligence = 12
wisdom = 13
charisma = 11

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('animal handling', 'athletics', 'deception', 'nature', 'perception', 'sleight of hand', 'stealth', 'survival')

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
feature_choices = ('Archery', 'Two-Weapon Fighting')

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()
_proficiencies_text = ()

# Proficiencies and languages
languages = """Common, Auran (Mimickry Only)"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ["Longbow", "Dagger", "Blunderbuss"]  # Example: ('shortsword', 'longsword')
magic_items = ['Decanter of Endless Water', 'Tooth of Animal Friendship',
               "Cape of the Mountebank", "Cloak of Billowing"]  # Example: ('ring of protection',)
armor = "Leather armor"  # Eg "light leather armor"
shield = "None"  # Eg "shield"

equipment = """Explorer's pack. Silver Necklace. Hunting Trap. Musical Instrument."""

attacks_and_spellcasting = """Arrows: d12

Blunderbuss: Range (15/60), Reload 1, Misfire 2

Buckshot: d6

+2 damage vs. beasts
"""

# List of known spells
# Example: spells = ('magic missile', 'mage armor')
spells = ("Detect Poison and Disease", "Hunter's Mark")

# Which spells have been prepared (not including cantrips)
spells_prepared = ("Detect Poison and Disease", "Hunter's Mark")

# Backstory
# Describe your backstory here
personality_traits = """

"""

ideals = """
Change

Inventor
"""

bonds = """
Children
"""

flaws = """
Don't save others
"""

features_and_traits = """"""
