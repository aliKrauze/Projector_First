from sqlalchemy import create_engine

username = 'useradd'
password = '1930'
host = '127.0.0.1'
database_name1 = 'airbnb'
port = 5432
connection_url1 = f'postgresql://{username}:{password}@{host}:{port}/{database_name1}'

engine = create_engine(connection_url1)
