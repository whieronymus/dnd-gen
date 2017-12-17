from random import randint
import sqlite3
from rollstats import roll_stats

conn = sqlite3.connect('characterdata.db')
c = conn.cursor()


def random_select(select):
    """
    Returns a randomly generated D&D 5e Class/Race/Background
    """
    list_build = []
    c.execute("SELECT * FROM character_data WHERE keyword = ?", (select,))
    for row in c.fetchall():
        list_build.append(row[1])

    return list_build[randint(0, len(list_build) - 1)]


def stat_by_class(c, i):
    """
    c is a 1 word string representing a character class
    i is a list of randomized attribute stats
    Returns a list sorted according to priority of what classes need
    """
    if c == 'Barbarian' or c == 'Fighter':
        i[1], i[2], i[3], i[4] = i[2], i[1], i[4], i[3]
    elif c == 'Bard' or c == 'Warlock' or c == 'Sorcerer':
        i[0], i[1], i[2], i[3], i[4], i[5] = \
        i[5], i[2], i[1], i[4], i[3], i[0]
    elif c == 'Druid' or c == 'Cleric':
        i[0], i[1], i[2], i[4] = i[2], i[4], i[1], i[0]
    elif c == 'Monk':
        i[0], i[1], i[2], i[3], i[4], i[5] = \
        i[3], i[0], i[2], i[5], i[1], i[4]
    elif c == 'Paladin':
        i[1], i[3], i[4], i[5] = i[4], i[5], i[3], i[1]
    elif c == 'Rogue':
        i[0], i[1], i[3], i[4], i[5] = i[5], i[0], i[1], i[3], i[4]
    elif c == 'Ranger':
        i[0], i[1], i[3], i[4], i[5] = i[3], i[0], i[4], i[1], i[5]
    elif c == 'Wizard':
        i[0], i[2], i[3], i[4], i[5] = i[5], i[3], i[0], i[2], i[4]

    return i


def race_adjust(r, i):
    """
    r is a string that represents the character's race
    i is a list of sorted prioritized attributes
    returns attributes with adjustments made based on racial features
    """
    if r == "Hill Dwarf":
        i[2] += 2
        i[4] += 1
    if r == "Mountain Dwarf":
        i[0] += 2
        i[2] += 2
    if r == "Drow":
        i[1] += 2
        i[5] += 1
    if r == "High Elf":
        i[1] += 2
        i[3] += 1
    if r == "Wood Elf":
        i[1] += 2
        i[4] += 1
    if r == "Lightfoot Halfling":
        i[1] += 2
        i[5] += 1
    if r == "Stout Halfling":
        i[1] += 2
        i[2] += 1
    if r == "Human":
        i[0] += 1
        i[1] += 1
        i[2] += 1
        i[3] += 1
        i[4] += 1
        i[5] += 1
    if r == "Dragonborn":
        i[0] += 2
        i[5] += 1
    if r == "Forest Gnome":
        i[3] += 2
        i[1] += 1
    if r == "Rock Gnome":
        i[3] += 2
        i[2] += 1
    if r == "Half-Elf":
        j = i.index(max(i[0:5]))
        i[j] += 1
        i_copy = i.copy()
        i_copy[j] = 0
        i[i.index(max(i_copy[0:5]))] += 1
        i[5] += 2
    if r == "Half-Orc":
        i[0] += 2
        i[2] += 1
    if r == "Tiefling":
        i[3] += 2
        i[5] += 1

    return i



def ability_modifier_list(ability_scores):
    """
    i is a list of ability scores after they're rolled, sorted, and racial
    bonus is applied
    returns a list of ability modifiers"""
    ability_modifiers = []
    for i in ability_scores:
        ability_modifiers.append((i-10)//2)

    return ability_modifiers

def skill_modifier(ability_scores):
    skill_list = []
    skill_list.append(ability_scores[1])
    skill_list.append(ability_scores[4])
    skill_list.append(ability_scores[3])
    skill_list.append(ability_scores[0])
    skill_list.append(ability_scores[5])
    skill_list.append(ability_scores[3])
    skill_list.append(ability_scores[4])
    skill_list.append(ability_scores[5])
    skill_list.append(ability_scores[3])
    skill_list.append(ability_scores[4])
    skill_list.append(ability_scores[3])
    skill_list.append(ability_scores[4])
    skill_list.append(ability_scores[5])
    skill_list.append(ability_scores[5])
    skill_list.append(ability_scores[3])
    skill_list.append(ability_scores[1])
    skill_list.append(ability_scores[1])
    skill_list.append(ability_scores[4])

    return skill_list

print('')
character_class = random_select("Class")
character_race = random_select("Race")
character_background = random_select("Background")
print("You are a " + character_race + " " + character_class + " " +
      character_background)
rolled_stats = roll_stats()
# print("Rolled Stats:     " + str(rolled_stats))
class_stat_sort = stat_by_class(character_class, rolled_stats)
# print("Sort by Class:    " + str(class_stat_sort))
add_racial_bonus = race_adjust(character_race, class_stat_sort)
# print("Add Racial Bonus: " + str(add_racial_bonus))
print('')
print("Strength: " + str(add_racial_bonus[0]))
print("Dexterity: " + str(add_racial_bonus[1]))
print("Constitution: " + str(add_racial_bonus[2]))
print("Intelligence: " + str(add_racial_bonus[3]))
print("Wisdom: " + str(add_racial_bonus[4]))
print("Charisma: " + str(add_racial_bonus[5]))

modifiers = ability_modifier_list(add_racial_bonus)
skill_list = skill_modifier(modifiers)

print('')
print('Acrobatics: ' + str(skill_list[0]))
print('Animal Handling: ' + str(skill_list[1]))
print('Arcana: ' + str(skill_list[2]))
print('Athletics: ' + str(skill_list[3]))
print('Deception: ' + str(skill_list[4]))
print('History: ' + str(skill_list[5]))
print('Insight: ' + str(skill_list[6]))
print('Intimidation: ' + str(skill_list[7]))
print('Investigation: ' + str(skill_list[8]))
print('Medicine: ' + str(skill_list[9]))
print('Nature: ' + str(skill_list[10]))
print('Perception: ' + str(skill_list[11]))
print('Performance: ' + str(skill_list[12]))
print('Persuasion: ' + str(skill_list[13]))
print('Religion: ' + str(skill_list[14]))
print('Sleight of Hand: ' + str(skill_list[15]))
print('Stealth: ' + str(skill_list[16]))
print('Survival: ' + str(skill_list[17]))
