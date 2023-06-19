#!/usr/bin/python3
"""script that lists all State objects that contain the letter a from the database"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    """ main entry point of the script that prints first state
        object """
    url_engine = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    engine = create_engine(url_engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%')).all()
    if states_with_a:
        for states in states_with_a:
            print('{0}: {1}'.format(states.id, states.name))
