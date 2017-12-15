from random import randint
import sqlite3
from rollstats import roll_stats


def class_generator():
    """
    Returns a randomly generated D&D 5e Class
    """
    with open('classlist.txt') as class_select:
        class_list = class_select.read().split(',')

    return class_list[randint(0,len(class_list) - 1)]


def race_generator():
    """
    Returns a randomly generated D&D 5e Race
    """
    with open('racelist.txt') as race_select:
        race_list = race_select.read().split(',')

    return race_list[randint(0,len(race_list) - 1)]


def stat_by_class(c, i):
    """
    c is a 1 word string representing a character class
    i is a list of randomized attribute stats
    Returns a list sorted according to priority of what classes need
    """
    if c == 'Barbarian' or c == 'Fighter':
        i[1], i[2], i[3], i[4] = i[2], i[1], i[4], i[3]
    elif c == 'Bard' or c == 'Warlock' or  c == 'Sorcerer':
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
    if r == "Half-ELf":
        i[0] += 1
        i[1] += 1
    if r == "Half-Orc":
        i[0] += 2
        i[2] += 1
    if r == "Tiefling":
        i[3] += 2
        i[5] += 1

    return i

character_class = class_generator()
character_race = race_generator()
print("You are a "+character_race + " " + character_class)
rolled_stats = roll_stats()
print("Rolled Stats:     " + str(rolled_stats))
add_racial_bonus = race_adjust(character_race, rolled_stats)
print("Add Racial Bonus: " + str(add_racial_bonus))
class_stat_sort = stat_by_class(character_class, add_racial_bonus)

print("Sort by Class:    " + str(class_stat_sort))
print("Strength: " + str(add_racial_bonus[0]))
print("Dexterity: " + str(add_racial_bonus[1]))
print("Constitution: " + str(add_racial_bonus[2]))
print("Intelligence: " + str(add_racial_bonus[3]))
print("Wisdom: " + str(add_racial_bonus[4]))
print("Charisma: " + str(add_racial_bonus[5]))
