#!/usr/bin/python3
"""This script lists states"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ = "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@hostname:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.agrv[3])

        session = sessionmaker(bind=engine)
