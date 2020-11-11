import sqlite3

with sqlite3.connect('./db.db') as conn:
    cur = conn.cursor()

cur.execute('CREATE TABLE name (id int)')
cur.execute('INSERT INTO name (id) values (1)')
r = cur.fetchall()

print(r)

