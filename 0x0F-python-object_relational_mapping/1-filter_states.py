#!/usr/bin/python3
"""
     lists all states with a name starting with N (upper N)
     from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY \
                name LIKE 'N%' ORDER BY id ASC")
    all_N_states = cur.fetchall()
    for n_states in all_N_states:
        print(n_states)
    cur.close()
    conn.close()
