#!/usr/bin/python3
""" script that lists all State objects from the database hbtn_0e_6_usa"""
if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    s = session.query(State).order_by(State.id).filter(State.name == 
                                                    argv[4]).first()    
    if s:
        print(s.id)
    else:
        print("Not found")
    session.close()
