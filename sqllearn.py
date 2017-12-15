import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    # Use all caps for SQL, regular casing for nonSQL
    c.execute('CREATE TABLE IF NOT EXISTS stuuToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')
