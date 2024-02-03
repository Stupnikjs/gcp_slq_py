import psycopg2

# Connection parameters
conn_params = {
    "sslmode": "require",  # Enforce SSL connection
    "sslrootcert": "server-ca.pem",
    "sslcert": "client-cert.pem",
    "sslkey": "client-key.pem",
    "hostaddr": "35.232.11.20",
    "port": "5432",
    "user": "postgres",
    "password": "postgres",
    "dbname": "postgres"

}

# Construct the connection string
conn_string = " ".join([f"{key}={value}" for key, value in conn_params.items()])

print(conn_string)

# Establish the connection
try:
    conn = psycopg2.connect(conn_string)
    print("Connection to PostgreSQL established successfully.")
    # Perform database operations here
except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)