import json

import sqlite3

fh = open('roster_data.json')

fh = fh.read()

data = json.loads(fh)



conn = sqlite3.connect('roster.db')
cur = conn.cursor()
cur.executescript('''

    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;

    CREATE TABLE User(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
    );

    CREATE TABLE Course(
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    title TEXT
    );

    CREATE TABLE Member(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    user_id INTEGER,
    course_id INTEGER,
    role TEXT
    );

''')

for j in data:
    if j is None:

        print('Here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        continue
    print(j[0])
    print(j[1])
    user = j[0]
    course = j[1]

    cur.execute('''INSERT OR IGNORE INTO User (name)
    VALUES (?)''', (j[0],))
    cur.execute('SELECT id FROM User WHERE name = ?', (j[0],))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
    VALUES (?)''', (j[1],))
    cur.execute('SELECT id FROM Course WHERE title = ?', (j[1],))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Member (user_id, course_id, role)
    VALUES ( ?, ?, ?)''', (user_id, course_id, j[2], ))

conn.commit()
