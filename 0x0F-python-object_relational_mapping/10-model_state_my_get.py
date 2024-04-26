#!/usr/bin/python3
"""
    script that prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa

    Your script should take 4 arguments: mysql username, mysql password,
    database name and state name to search (SQL injection free)
    You must use the module SQLAlchemy
    You must import State and Base from model_state -
    from model_state import Base, State
    Your script should connect to a MySQL server running on
    localhost at port 3306
    You can assume you have one record with the state name to search
    Results must display the states.id
    If no state has the name you searched for, display Not found
    Your code should not be executed when imported
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    state_name = argv[4]
    check_state_name = state_name.split()
    if (len(check_state_name) > 1):
        exit(1)

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           user, passwd, db))
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).filter_by(name=state_name):
        print(instance.id)
        exit()
    print("Not found")
