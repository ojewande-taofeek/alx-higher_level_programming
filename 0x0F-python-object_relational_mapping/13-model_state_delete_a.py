#!/usr/bin/python3
"""
    deletes all State objects with a name containing
    the letter a from the database hbtn_0e_6_usa
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
    all_a_states = session.query(State).filter(State.name.like("%a%"))
    for a_state in all_a_states:
        session.delete(a_state)
    session.commit()
