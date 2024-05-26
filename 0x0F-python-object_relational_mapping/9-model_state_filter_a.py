#!/usr/bin/python3
"""
    lists all State objects that contain the letter a from
    the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            user, passwd, db))
    Base.metadata.create_all(engine)  # this may not be needed in this program
    Session = sessionmaker(bind=engine)
    session = Session()
    a_states = session.query(State).order_by(State.id).filter(
               State.name.like("%a%"))
    for a_state in a_states:
        print("{}: {}".format(a_state.id, a_state.name))
