#!/usr/bin/python3
"""Python file similar to model_state.py named model_city.py that contains the class definition of a City."""

if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_city import City
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    Base.metadata.create_all(engine)
    
    print_c = session.query(State, City).select_from(State).join(City, State.id == City.state_id).order_by(City.id).all()
    for state, city in print_c:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()