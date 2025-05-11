from sqlalchemy import create_engine # used to connect to a db
from sqlalchemy import text

engine = create_engine('sqlite:///mydatabase.db', echo=True)

conn = engine.connect()

# * Execute Custom queries
conn.execute(text("CREATE TABLE IF NOT EXISTS people (name str, age int)"))
conn.commit()


# * Execute Custom queries using Session
from sqlalchemy.orm import Session
session = Session(engine)

session.execute(text('INSERT INTO people (name, age) VALUES ("Mike", 30);'))
session.commit