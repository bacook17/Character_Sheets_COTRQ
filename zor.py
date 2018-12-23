"""This file describes the heroic adventurer Zor Daar.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.0"

name = "Zor Daar"
player_name = "Harshil"

# Be sure to list Primary class first
classes = ['Paladin']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [3]  # ex: [10] or [3, 2]
subclasses = ['']  # ex: ['Necromacy'] or ['Thief', None]
background = "Soldier"
race = "Human"
alignment = "Chaotic Good"

xp = 0
hp_max = 33
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 16
dexterity = 12
constitution = 13
intelligence = 11
wisdom = 9
charisma = 13

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('athletics', 'intimidation', 'persuasion', 'religion')

# Named features / feats that aren't part of your classes,
# race, or background. Also include Eldritch Invocations.
# Example:
# features = ('Tavern Brawler',)  # take the optional Feat from PHB
features = ()

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

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
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ["Greatsword", "War pick", "Javelin"] # Example: ('shortsword', 'longsword')
magic_items = []  # Example: ('ring of protection',)
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
*Divine Sense: evil smells bad. As an action, can open awareness to detect evil forces. 
Can use 1+CHA times before Long Rest.

*Lay on Hands: Healing power of touch. Pool of HP = 5xLVL

*Military Rank

*Great Weapon Fighting: Reroll 1 or 2 on damage dice

*Divine Smite: 2d8 radiant / 1st-level spell slot

*Immune to Disease

*5 followers
"""
