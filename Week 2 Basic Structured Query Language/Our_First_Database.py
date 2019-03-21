import sqlite3

conn = sqlite3.connect('sqlite32.db')
cur = conn.cursor()

cur.executescript('''
    CREATE TABLE Ages (
        name VARCHAR(128),
        age INTEGER
    );

    DELETE FROM Ages;
    INSERT INTO Ages (name,age) VALUES ('Laibah',17);
    INSERT INTO Ages (name,age) VALUES ('Jessie',18);
    INSERT INTO Ages (name,age) VALUES ('Pascoe',40);
    INSERT INTO Ages (name,age) VALUES ('Ellenor',38);
    INSERT INTO Ages (name,age) VALUES ('Brandyn',15);
    INSERT INTO Ages (name,age) VALUES ('Kayla',13);

    SELECT hex(name || age) AS X FROM Ages ORDER BY X;
''')

cur.close()
