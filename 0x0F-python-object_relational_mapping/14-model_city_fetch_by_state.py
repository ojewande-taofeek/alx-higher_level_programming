#!/usr/bin/python3
"""
    prints all City objects from the database hbtn_0e_14_usa
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            user, passwd, db))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    all_states = session.query(
                 State).join(City, State.id == City.state_id).order_by(
                         City.id).all()
    for state in all_states:  # to get all state
        for city in state.city:  # access the the city through class att city
            print("{}: ({}) {}".format(state.name, city.id, city.name))
