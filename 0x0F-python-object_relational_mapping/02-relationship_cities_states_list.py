#!/usr/bin/python3

if __name__ == '__main__':
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy.orm import sessionmaker, relationship
    from sqlalchemy import create_engine
    import sys
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                            sys.argv[2],
                                                            sys.argv[3]))
    
