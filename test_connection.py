import psycopg2
from psycopg2 import OperationalError
from vars import USERNAME, PASSWORD


def connect_to_db():
    try:
        # Setup the connection parameters
        params = {
            "host": "10.32.25.124",
            "port": 5432,
            "dbname": "prd",
            "user": USERNAME,
            "password": PASSWORD,
        }

        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**params)

        # Create a cursor object
        cursor = conn.cursor()

        # Execute a simple SQL query
        cursor.execute("SELECT version();")

        # Fetch the result
        record = cursor.fetchone()

        # Print the result
        print("You are connected to - ", record)

        # Close the cursor and connection
        cursor.close()
        conn.close()

        print("Connection closed.")

    except OperationalError as e:
        print(f"The error '{e}' occurred")


if __name__ == "__main__":
    connect_to_db()
