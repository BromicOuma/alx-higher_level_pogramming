#!/usr/bin/python3
"""script that prints the State object with the
    name passed as argument from the database hbtn_0e_6_usa """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """prints the state object with name passed as argument """
    engine_connect = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    engine = create_engine(engine_connect)

    Session = sessionmaker(bind=engine)

    session = Session()

    search_name = argv[4]

    results = session.query(State).filter_by(name=search_name).first()

    if results:
        print('{0}'.format(results.id))
    else:
        print("Not found")
