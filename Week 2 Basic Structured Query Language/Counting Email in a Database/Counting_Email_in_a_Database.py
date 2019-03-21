import re
import sqlite3

fh = open('C:/Users/Jeremiah/Desktop/Coursera Using Databases with Python/Week 2 Basic Structured Query Language/Counting Email in a Database/mbox.txt')

lst = []
for line in fh:
    if not line.startswith('From '):
        continue
    email = line.split()[1]
    org = re.findall(r'@\S+',email)
    org = org[0]
    org = org[1:len(org)]
    lst.append(org)

tuple_lst = []
ans_lst = []

for i in lst:
    tuple_lst.append((i,lst.count(i)))

for q in tuple_lst:
    if q in ans_lst:
        continue
    else:
        ans_lst.append(q)

def sec_elem(s):
    return s[1]

ans_lst = sorted(ans_lst, key = sec_elem)
ans_lst.reverse()



conn = sqlite3.connect('email_lst.db')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Counts;
CREATE TABLE Counts (org TEXT, count INTEGER);
''')

for z in ans_lst:
    cur.execute('''
    INSERT INTO Counts (org, count)
    VALUES (?,?) ''',(z[0], z[1]))
    print(z[0])
    print(z[1])

conn.commit()
