#!/usr/bin/python3
"""
Prints the State object with the name
 passed as arguement from the database hbtn_0e_6_usa
"""
if __name__ == '__main__':
    import sqlalchemy
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State(name = 'Louisiana')
    session.add(newState)
    session.flush()
    print("{}".format(newState.id))
    session.close()
