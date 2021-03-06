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
    from sqlalchemy.ext.declarative import declarative_base

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter(State.id == 2).\
        update({State.name: "New Mexico"}, synchronize_session=False)
    session.commit()
    session.close()
