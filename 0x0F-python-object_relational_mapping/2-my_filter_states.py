#!/usr/bin/python3
"""
    takes in an argument and displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument.
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name \
                LIKE '{}'".format(argv[4]))
    all_input_states = cur.fetchall()
    for input_state in all_input_states:
        print(input_state)
    cur.close()
    conn.close()
