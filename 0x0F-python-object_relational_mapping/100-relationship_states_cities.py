#!/usr/bin/python3
"""Python file similar to model_state.py named model_city.py that contains the class definition of a City."""

if __name__ == '__main__':
    from relationship_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from relationship_city import City
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    new_state = State(name="California")
    new_city = City("San Francisco")
    new_state.cities.append(new_city)
    session.add_all([new_state, new_city])
    session.commit()
    session.close()