import sqlite3
import time
import datetime



conn = sqlite3.connect('characterdata.db')
c = conn.cursor()

def create_table():
    # Use all caps for SQL, regular casing for nonSQL
    c.execute('CREATE TABLE IF NOT EXISTS character_race(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')


def data_entry(data_input):
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Race'
    value = data_input

    c.execute("INSERT INTO character_race(unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
          (unix, date, keyword, value))

    conn.commit()

create_table()

class_list = ['Barbarian', 'Bard', 'Druid', 'Fighter', 'Monk', 'Ranger',
              'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
race_list = ['Hill Dwarf', 'Mountain Dwarf', 'Drow', 'High Elf', 'Wood Elf',
             'Lightfoot Halfling', 'Stout Halfling', 'Human', 'Dragonborn',
             'Forest Gnome', 'Rock Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling']
for i in race_list:
    data_entry(i)

c.close
conn.close()
