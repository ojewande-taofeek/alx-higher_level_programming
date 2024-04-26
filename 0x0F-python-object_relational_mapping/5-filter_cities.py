#!/usr/bin/python3
"""
    script that takes in the name of a state as an argument and lists all
    cities of that state, using the database hbtn_0e_4_usa
    Your script should take 4 arguments: mysql username, mysql password,
    database name and state name (SQL injection free!)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost at
    port 3306
    Results must be sorted in ascending order by cities.id
    You can use only execute() once
    The results must be displayed as they are in the example below
    Your code should not be executed when imported
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    myList = argv[4].split()
    if len(myList) != 1:
        exit(1)
    input_num = cur.execute("""
                            SELECT cities.name FROM cities INNER JOIN states
                            ON state_id=states.id WHERE states.name=%s
                            ORDER BY state_id ASC
                            """, (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        tuple_to_str = (str(row).replace('(', "").replace(')', ""))
        tuple_to_str = tuple_to_str.replace("'", "").replace(",", "")
        if input_num == 1:
            print(tuple_to_str)
            break
        print(tuple_to_str, end=", ")
        input_num = input_num - 1
    cur.close()
    conn.close()
