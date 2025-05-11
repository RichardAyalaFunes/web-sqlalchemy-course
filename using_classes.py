from sqlalchemy import create_engine, Integer, String, Float, Column, ForeignKey, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# engine = create_engine('sqlite:///mydatabase.db', echo=True)
engine = create_engine('postgresql://postgres:postgres@localhost:5433/sql_tutorial', echo=True)

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    
    things = relationship('Thing', back_populates='person')
    
class Thing(Base):
    __tablename__ = 'things'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    value = Column(Float)
    owner = Column(Integer, ForeignKey('people.id'))
    
    person = relationship('Person', back_populates='things')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# * Selecting ->
# result = session.query(Person.name, Person.age).all()
# print(result)

# result = session.query(Person).filter(Person.age > 40).all()
# print([t.name for t in result])

# result = session.query(Person.name, Thing.description).join(Thing).all() # Joining
result = session.query(Thing.owner, func.sum(Thing.value)).group_by(Thing.owner).having(func.sum(Thing.value) > 50).all() # Advanced Joining
print(result)

# * Update ->
# result = session.query(Person).filter(Person.name == 'Charlie').update({'name': 'Charles'})
# session.commit()
# result = session.query(Person).filter(Person.name == 'Charles')
# print([t.name for t in result])

# * Deleting ->
# result = session.query(Thing).filter(Thing.value < 50).delete()
# session.commit()
# result = session.query(Thing).filter(Thing.value < 50).all()
# print([t.description for t in result])

# * Creating ->
# # Add User
# new_person = Person(name='Charlie', age=70)
# session.add(new_person)
# session.flush()
# # Add Thing
# new_thing = Thing(description='Camera', value=500, owner=new_person.id)
# session.add(new_thing)

# session.commit()

# print([t.description for t in new_person.things])
# print(new_thing.person.name)