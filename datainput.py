import sqlite3
import time
import datetime



conn = sqlite3.connect('characterdata.db')
c = conn.cursor()

def create_table():
    # Use all caps for SQL, regular casing for nonSQL
    c.execute('CREATE TABLE IF NOT EXISTS character_data(keyword TEXT,\
    value REAL)')


def data_entry(keyword, data_input):
    c.execute("INSERT INTO character_data(keyword, value)\
              VALUES (?, ?)", (keyword, data_input))

    conn.commit()

create_table()

class_list = ['Barbarian', 'Bard', 'Druid', 'Fighter', 'Monk', 'Ranger',
              'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
race_list = ['Hill Dwarf', 'Mountain Dwarf', 'Drow', 'High Elf', 'Wood Elf',
             'Lightfoot Halfling', 'Stout Halfling', 'Human', 'Dragonborn',
             'Forest Gnome', 'Rock Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling']
for i in class_list:
    data_entry('Class', i)

c.close
conn.close()
