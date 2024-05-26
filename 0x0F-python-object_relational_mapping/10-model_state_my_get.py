#!/usr/bin/python3
"""
    prints the State object with the name passed as argument
    from the database hbtn_0e_6_usa
    otherwise, print 'Nothing'
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    if len(argv[4].split()) > 2:
        exit()
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            user, passwd, db))
    Base.metadata.create_all(engine)  # this may not be needed in this program
    Session = sessionmaker(bind=engine)
    session = Session()
    passed_state = session.query(State).order_by(State.id).filter(
                   State.name.like(argv[4]))
    if passed_state.count() == 0:
        print("Not found")
    else:
        for state in passed_state:
            print(state.id)
