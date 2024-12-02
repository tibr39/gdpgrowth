import pandas as pd
from sqlalchemy import create_engine
#this converts the dataset to PostgreSQl
engine = create_engine('postgresql://postgres:kapitany@localhost:5432/postgres')
df=pd.read_csv('countriesecoindexes.csv')
df.to_sql('countryindexes', engine, if_exists='replace')
