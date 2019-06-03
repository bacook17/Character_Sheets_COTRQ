"""This file describes the heroic adventurer Zeed.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.2"

name = "Zeed"
player_name = "Tarraneh"

# Be sure to list Primary class first
classes = ['Cleric']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [6]  # ex: [10] or [3, 2]
subclasses = ["Tempest Domain"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Sage"
race = "Aarakocra"
alignment = "Chaotic good"

xp = 0
hp_max = 39
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 12
dexterity = 18
constitution = 12
intelligence = 8
wisdom = 12
charisma = 11

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('arcana', 'history', 'medicine', 'persuasion')

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
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()
_proficiencies_text = ()

# Proficiencies and languages
languages = """Common, Aarakocra, Auran, Giant, Elvish"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ["Warhammer", "Light crossbow"]  # Example: ('shortsword', 'longsword')
magic_items = ["Eyes of Charming", "Shield of Faces", "Coins of Communication"]  # Example: ('ring of protection',)
armor = "Leather armor"  # Eg "light leather armor"
shield = "Shield of Faces"  # Eg "shield"

equipment = """Priests' pack, amulet, DA Coin"""

attacks_and_spellcasting = """Bolts: d12

+2 Bolts: d6

(AC = 15 if using crossbow - no shield)
"""

# List of known spells
# Example: spells = ('magic missile', 'mage armor')
spells = ("Guidance", "Resistance", "Spare the Dying", "Thaumaturgy",
          "Cure Wounds", "Bane", "Guiding Bolt",
          "Mirror Image", "Hold Person", "Enhance Ability",
          "Aura of Vitality")

# Which spells have been prepared (not including cantrips)
spells_prepared = spells

# Backstory
# Describe your backstory here
personality_traits = """
Help others
"""

ideals = """
Self Improvement
"""

bonds = """
"""

flaws = """
Speak without thinking
"""

features_and_traits = """
"""
