"""This file describes the heroic adventurer Celadin.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.0"

name = "Celadin"
player_name = "Lehman"

# Be sure to list Primary class first
classes = ['Warlock']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [3]  # ex: [10] or [3, 2]
subclasses = ["The Fiend Patron"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Far Traveler"
race = "Fallen Aasimar"
alignment = "Lawful good"

xp = 0
hp_max = 15
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 13
dexterity = 11
constitution = 8
intelligence = 10
wisdom = 12
charisma = 17

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('arcana', 'insight', 'intimidation', 'perception')

# Named features / feats that aren't part of your classes,
# race, or background. Also include Eldritch Invocations.
# Example:
# features = ('Tavern Brawler',)  # take the optional Feat from PHB
features = ("Eldritch Sight", "Eyes of the Rune Keeper")

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()
_proficiencies_text = ()

# Proficiencies and languages
languages = """Dwarvish, Common, Celestial"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ["Dagger", "Quarterstaff", "Spear"] # Example: ('shortsword', 'longsword')
magic_items = []  # Example: ('ring of protection',)
armor = "Leather armor"  # Eg "light leather armor"
shield = "None"  # Eg "shield"

equipment = """Staff (focus). Dungeoneer's Pack. Chess set.
Piece of Jewelry (10 GP)"""

attacks_and_spellcasting = """"""

# List of known spells
# Example: spells = ('magic missile', 'mage armor')
spells = ("Burning Hands", "Command", "Eldritch Blast", "Darkness",
          "Detect Magic", "Enthrall", "Hellish Rebuke", "Hex", "Hold Person",
          "Illusory Script", "Invisibility", "Light", "Mage Hand",
          "Misty Step", "Shatter", "Spider Climb", "Unseen Servant",
          "Suggestion", "Detect Magic")

# Which spells have been prepared (not including cantrips)
spells_prepared = ("Command", "Darkness", "Hellish Rebuke", "Detect Magic",
                   "Eldritch Blast", "Hex", "Light", "Mage Hand", "Misty Step",
                   "Detect Magic")

# Backstory
# Describe your backstory here
personality_traits = """
Proud.
Prone to literally state feelings.
Tries to relax people with ASMR.
"""

ideals = """
Obeys celestial guardian.
"""

bonds = """
Wants to bring his family home.
"""

flaws = """
"""

features_and_traits = """*Resist Necrotic & Radiant.

*Heal LvL HP with touch (action).

*Dark One's Blessing (temp HP = CHA + LVL on kill).

*All eyes on you.

*Eldritch sight: detect magic.

*Eyes of the Rune Keeper: read all writing.
"""
