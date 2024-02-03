from sqlalchemy import create_engine, MetaData, Table, text
import pandas as pd 

# Connection parameters
conn_params = {
    "sslmode": "require",  # Enforce SSL connection
    "sslrootcert": "server-ca.pem",
    "sslcert": "client-cert.pem",
    "sslkey": "client-key.pem",
    "host": "35.232.11.20",
    "port": "5432",
    "user": "postgres",
    "password": "postgres",
    "database": "postgres"
}

# Construct the connection string
conn_str = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(**conn_params)

# Create the SQLAlchemy engine
engine = create_engine(conn_str)

# Establish the connection
with engine.connect() as conn:
    res = conn.execute(text('SELECT title FROM house;'))
    for row in res: 
        print(row)


# Execute SQL queries
# df = pd.read_csv('output.csv')
# df.to_sql('house', con=engine, index=False, if_exists='replace')


    