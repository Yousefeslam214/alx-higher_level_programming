#!/usr/bin/python3
"""sqlalchemy"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/alchemy', echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()
    found = False
    StateQuery = session.query(State).filter(State.name == sys.argv[4]).first()
    if StateQuery:
        print("{}".format(StateQuery.id))
    else:
        print("Not found")
