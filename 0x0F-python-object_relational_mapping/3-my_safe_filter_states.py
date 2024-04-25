#!/usr/bin/python3
"""
    script that takes in arguments and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
    But this time, write one that is safe from MySQL injections!
    Your script should take 4 arguments: mysql username, mysql password,
    database name and state name searched (safe from MySQL injection)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost
    at port 3306
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported
"""
import MySQLdb
from sys import argv


conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                       passwd=argv[2], db=argv[3])
cur = conn.cursor()
myList = argv[4].split()
if len(myList) != 1:
    exit(1)
cur.execute("SELECT * FROM states WHERE name = %s", (argv[4],))
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()
