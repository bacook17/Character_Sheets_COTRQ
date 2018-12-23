"""This file describes the heroic adventurer Ma'caw.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.0"

name = "Ma'caw"
player_name = "Ashley"

# Be sure to list Primary class first
classes = ['Revised Ranger']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [3]  # ex: [10] or [3, 2]
subclasses = ["Beast Conclave"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Outlander"
race = "Kenku"
alignment = "Neutral"

xp = 0
hp_max = 22
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
skill_proficiencies = ('animal handling', 'athletics', 'deception', 'nature',
                       'perception', 'sleight of hand', 'stealth', 'survival')

# Named features / feats that aren't part of your classes,
# race, or background. Also include Eldritch Invocations.
# Example:
# features = ('Tavern Brawler',)  # take the optional Feat from PHB
features = ()

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ('Archery',)

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
weapons = ["Longbow", "Dagger", "Blunderbuss"] # Example: ('shortsword', 'longsword')
magic_items = []  # Example: ('ring of protection',)
armor = "Leather armor"  # Eg "light leather armor"
shield = "None"  # Eg "shield"

equipment = """Explorer's pack. Cloack of billowing. Decanter of Endless Water.
Wolf's Tooth. Silver Necklace. Hunting Trap. Musical Instrument."""

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

features_and_traits = """
*Expert Forgery

*Mimicry

*Wanderer

*Favored Enemy: Beasts. ADV on survival to track, extra damage.

*Natural Explorer: Ignore difficult terrain. ADV on initiative.
On first turn in combat, ADV versus creatures that haven't acted.

-Traveling for 1+ hours: Difficult terrain doesn't slow your group. Your group
can't become lost except by magical means. Remain alert to danger even if preoccupied.
If traveling alone, can move stealthily at normal pace. When you forage, find
2x food as normal. When tracking other creatures, you learn exact number, sizes,
and how long ago they passed through the area.
"""
