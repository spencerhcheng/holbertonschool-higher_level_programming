#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
if __name__ == '__main__':
    import sqlalchemy
    import sys
    from model_state import Base, State
    from model_city import Base, City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for cities in session.query(City, State).\
        filter(City.state_id == State.id).order_by(City.id).all():
                print("{}: ({}) {}".format(cities.State.name,
                                           cities.City.id, cities.City.name))
