from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert, Float, ForeignKey, func

# engine = create_engine('sqlite:///mydatabase.db', echo=True)
engine = create_engine('postgresql://postgres:postgres@localhost:5433/sql_tutorial', echo=True)

meta = MetaData()

people = Table(
    "people", 
    meta, 
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('age', Integer),
)

things = Table(
    "things",
    meta, 
    Column('id', Integer, primary_key=True),    
    Column('description', String, nullable=False),    
    Column('value', Float),    
    Column('owner', Integer, ForeignKey('people.id')),    
)

meta.create_all(engine)

conn = engine.connect()

# * - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# * BASICS 2 -> 
insert_people = people.insert().values([
    {'name': 'Mike', 'age': 30},
    {'name': 'Bob', 'age': 35},
    {'name': 'Anna', 'age': 38},
    {'name': 'John', 'age': 50},
    {'name': 'Clara', 'age': 42},
])

insert_things = things.insert().values([
    {'owner': 24, 'description': 'Laptop', 'value': 800.0},
    {'owner': 24, 'description': 'Mouse', 'value': 50.50},
    {'owner': 24, 'description': 'Keyboard', 'value': 100.50},
    {'owner': 25, 'description': 'Book', 'value': 30},
    {'owner': 26, 'description': 'Bottle', 'value': 10.50},
    {'owner': 27, 'description': 'Speakers', 'value': 80.05},
])
# Create data
# conn.execute(insert_people)
# conn.commit()
# conn.execute(insert_things)
# conn.commit()

# * Select with "join" and "outer join"
# join_statement = people.join(things, people.c.id == things.c.owner) # Option 1
# join_statement = people.outerjoin(things, people.c.id == things.c.owner) # Option 2
# select_statement = people.select().with_only_columns(people.c.name, things.c.description).select_from(join_statement)
# result = conn.execute(select_statement)
#
# for row in result:
#     print(row)

# * Select GroupBy and SUM
# group_by_statement = things.select().with_only_columns(things.c.owner, func.sum(things.c.value)).group_by(things.c.owner)
# group_by_statement = things.select().with_only_columns(things.c.owner, func.sum(things.c.value)).group_by(things.c.owner).having(func.sum(things.c.value) > 50)
# result = conn.execute(group_by_statement)

# for row in result.fetchall():
#     print(row)

# * - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# * BASICS 1 ->

# * Insert data
# insert_statement = insert(people).values(name='Jane', age=40) # Opcion 1 - using INSERT
# insert_statement = people.insert().values(name='Mike', age=30) # Opcion 2 - using the TABLE
# result = conn.execute(insert_statement)
# conn.commit()

# * Select data
# select_statement = people.select().where(people.c.age > 20)
# result = conn.execute(select_statement)

# for row in result.fetchall():
#     print(row)
    
# * Update data
# update_state = people.update().where(people.c.name == 'Mike').values(age=99)
# result = conn.execute(update_state)
# conn.commit()

# * Delete data
# delete_state = people.delete().where(people.c.name == 'Mike')
# result = conn.execute(delete_state)
# conn.commit()