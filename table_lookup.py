import psycopg2
from vars import DB, USERNAME, PASSWORD, HOST, PORT

# Connect to the database
conn = psycopg2.connect(dbname=DB, user=USERNAME, password=PASSWORD, host=HOST)
cursor = conn.cursor()

# Check if the table exists using pg_tables
cursor.execute(
    "SELECT EXISTS (SELECT FROM pg_tables WHERE tablename = 'the_gary_null_show');"
)
exists = cursor.fetchone()[0]

# Alternatively, check using information_schema.tables
# cursor.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'the_gary_null_show' AND table_schema = 'public');")
# exists = cursor.fetchone()[0]

# Close the cursor and connection
cursor.close()
conn.close()

print(f"Table exists: {exists}")
