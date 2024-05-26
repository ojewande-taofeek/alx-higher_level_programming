#!/usr/bin/python3
"""
    lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


user = argv[1]
passwd = argv[2]
db = argv[3]
engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                        user, passwd, db))
Session = sessionmaker(bind=engine)
session = Session()
all_states = session.query(State).all()
for state in all_states:
    print("{}: {}".format(state.id, state.name))
