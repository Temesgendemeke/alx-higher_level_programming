#!/usr/bin/python3
"""Python file similar to model_state.py named model_city.py that contains the class definition of a City."""

if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_city import City
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    Base.metadata.create_all(engine)
    
    print_c = session.query(City, State).join(State, City.state_id == State.id).order_by(City.id).all()
    for s, c in print_c:
        print("{:} ({}) {}".format(c.name, c.id, s.name))

    
    session.close()