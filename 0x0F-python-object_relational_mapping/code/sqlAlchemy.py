from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import or_

engine = create_engine('postgresql://postgres:postgres@localhost:5432/alchemy', echo=False)
#engine = create_engine('postgresql://username:password@localhost:5432/database_name', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class State(Base):
    """State class"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

Base.metadata.create_all(engine)
state1 = State(id=1,name='yousef')
session.add(state1)
state2 = State(id=2,name='nyouadfsfsef')
session.add(state2)
state3 = State(id=3,name='ayouafdafasfsef')
session.add(state3)
sssd = session.query(State).filter(State.name=="yousef").first()
print(sssd.name, sssd.id)
print("---------")
sssf = session.query(State).filter(or_(State.name == "ayouafdafasfsef", State.name == "yousef")).all()
for state in sssf:
    print(state.name, state.id)
print("---------")
sss = session.query(State).order_by(State.id)
for s in sss:
    print(s.id ,end=': ')
    print(s.name)
sssdel = session.query(State).filter(State.name=="yousef").first()
session.delete(sssdel)
print("---------")
sss = session.query(State).order_by(State.id)
for s in sss:
    print(s.id ,end=': ')
    print(s.name)
print("---------")
print("done")



session.commit()
