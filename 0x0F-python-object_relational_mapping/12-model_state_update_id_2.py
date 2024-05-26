#!/usr/bin/python3
"""
    changes the name of a State object from the database hbtn_0e_6_usa
    Change the name of the State where id = 2 to New Mexico
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
    obj_2 = session.query(State).filter_by(id=2).first()
    obj_2.name = "New Mexico"
    session.add(obj_2)
    session.commit()
