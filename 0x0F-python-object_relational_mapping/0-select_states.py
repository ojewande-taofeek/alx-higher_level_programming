#!/usr/bin/python3
"""
     lists all states from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states order by id ASC")
    all_states = cur.fetchall()
    for state in all_states:
        print(state)
    cur.close()
    conn.close()
