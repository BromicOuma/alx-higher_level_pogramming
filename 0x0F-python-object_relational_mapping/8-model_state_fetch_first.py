#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa"""

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

    first_object = session.query(State).first()
    if first_object:
        print('{0}: {1}'.format(first_object.id, first_object.name))
