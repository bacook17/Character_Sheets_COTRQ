"""This file describes the heroic adventurer Celadin.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.2"

name = "Celadin"
player_name = "Lehman"

# Be sure to list Primary class first
classes = ['Warlock']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [7]  # ex: [10] or [3, 2]
subclasses = ["The Fiend Patron"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Far Traveler"
race = "Fallen Aasimar"
alignment = "Lawful good"

xp = 0
hp_max = 28
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 14
dexterity = 11
constitution = 8
intelligence = 10
wisdom = 12
charisma = 18

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('arcana', 'insight', 'intimidation', 'perception')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = []

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ["Eldritch Sight", "Cloak of Flies", 'Voice of the Chain Master']

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ('Pact of the Chain',)

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()
_proficiencies_text = ("chess", "ASMR",)

# Proficiencies and languages
languages = """Dwarvish, Common, Celestial"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 1400
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ["Dagger", "Quarterstaff", "Spear of Lightning"]  # Example: ('shortsword', 'longsword')
magic_items = ["Coins of Communication", "Pipe of Smoke Monsters", 'Spear of Lightning']  # Example: ('ring of protection',)
armor = "Studded Leather armor +1"  # Eg "light leather armor"
shield = "None"  # Eg "shield"

equipment = """Staff (focus). Dungeoneer's Pack. Chess set.
Piece of Jewelry (10 GP). 2 bloodstones, 1 Moonstone, 10 large rubies, 6 large emeralds, 10 pearl/topaz/shell necklaces.
2x potions, Map of Sumber Hills
"""

attacks_and_spellcasting = """
Lightning Spear: command word "Caranda!"
"""

# List of known spells
# Example: spells = ('magic missile', 'mage armor')
spells = ("Eldritch Blast", "Mage Hand", "Chill Touch",
          "Command", "Hex",
          "Darkness", "Misty Step",
          "Dispel Magic", "Remove Curse", "Hunger of Hadar")
          # "Burning Hands", "Command", "Hex", "Illusory Script", "Unseen Servant",
          # "Enthrall", "Darkness", "Hold Person", "Invisibility", "Misty Step", "Shatter", "Spider Climb", "Suggestion",
          # "Dispel Magic", "Remove Curse", "Hunger of Hadar")

# Which spells have been prepared (not including cantrips)
spells_prepared = spells

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

features_and_traits = """
TODO: One 4th Level Spell Known

4th Eldritch Invocation
"""
