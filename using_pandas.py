import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5433/sql_tutorial', echo=True)

df = pd.read_sql("SELECT * FROM people", con=engine)

print(df)

# * Creating -> 
# new_data = pd.DataFrame({'name': ['Florian', 'Jack'], 'age':[26, 90]})
# new_data.to_sql('people', con=engine, if_exists='append', index=False)