from random import randint
from rollstats import roll_stats

def class_generator():
    """
    Returns a randomly generated D&D 5e Class
    """
    with open('classlist.txt') as class_select:
        class_list = class_select.read().split(',')

    return class_list[randint(0,len(class_list) - 1)]

def stat_by_class(c, i):
    """
    c is a 1 word string representing a character class
    i is a list of randomized attribute stats
    Returns a list sorted according to priority of what classes need
    """
    if c == 'Barbarian' or c == 'Fighter':
        i[1], i[2], i[3], i[4] = i[2], i[1], i[4], i[3]
    elif c == 'Bard' or c == 'Warlock' or  c == 'Sorcerer':
        i[0], i[1], i[2], i[3], i[4], i[5] = i[5], i[2], i[1], i[4], i[3], i[0]
    elif c == 'Druid' or c == 'Cleric':
        i[0], i[1], i[2], i[4] = i[2], i[4], i[1], i[0]
    elif c == 'Monk':
        i[0], i[1], i[2], i[3], i[4], i[5] = i[3], i[0], i[2], i[5], i[1], i[4]
    elif c == 'Paladin':
        i[1], i[3], i[4], i[5] = i[4], i[5], i[3], i[1]
    elif c == 'Rogue':
        i[0], i[1], i[3], i[4], i[5] = i[5], i[0], i[1], i[3], i[4]
    elif c == 'Ranger':
        i[0], i[1], i[3], i[4], i[5] = i[3], i[0], i[4], i[1], i[5]

    return i


character_class = class_generator()
print("You are a " + character_class)
rolled_stats = roll_stats()
class_stat_sort = stat_by_class(character_class, rolled_stats)
print("Strength: " + str(class_stat_sort[0]))
print("Dexterity: " + str(class_stat_sort[1]))
print("Constitution: " + str(class_stat_sort[2]))
print("Intelligence: " + str(class_stat_sort[3]))
print("Wisdom: " + str(class_stat_sort[4]))
print("Charisma: " + str(class_stat_sort[5]))
