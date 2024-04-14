#!/usr/bin/python3
"""This script adds a new state to the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    new = session.query(State).filter_by(id=2).first()
    new.name = "New Mexico"
    session.commit()
    print(new.name)
