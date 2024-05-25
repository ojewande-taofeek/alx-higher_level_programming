#!/usr/bin/python3
"""
     takes in the name of a state as an argument and
     lists all cities of that state, using the database hbtn_0e_4_usa
     SQL injection free
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    if len(argv[4].split()) != 1:
        exit()
    cur.execute("SELECT name FROM cities \
                 WHERE state_id=(SELECT id FROM states \
                 WHERE BINARY name LIKE '{}')".format(argv[4]))
    selected_cities = cur.fetchall()
    counter = cur.rowcount
    for city in selected_cities:
        city = str(city[0])
        if counter == 1:
            print("{}".format(city))
            break
        else:
            print("{}, ".format(city), end="")
        counter -= 1
    cur.close()
    conn.close()
