#!/usr/bin/python3
"""
    script that adds the State object “Louisiana” to the database
    hbtn_0e_6_usa

    Your script should take 3 arguments: mysql username, mysql password
    and database name
    You must use the module SQLAlchemy
    You must import State and Base from model_state -
    from model_state import Base, State
    Your script should connect to a MySQL server running on
    localhost at port 3306
    Print the new states.id after creation
    Your code should not be executed when imported
"""
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)    # session.add(State(name="Louisiana")) works too
    session.commit()
    for instance in session.query(State).filter_by(name="Louisiana"):
        print(instance.id)
    session.close()
