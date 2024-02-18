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

    delete_s = session.query(State).order_by(State.id).filter(State.name.like('%a%'))
    for del_state in delete_s:
        session.delete(del_state)
        session.commit()
    session.close()
