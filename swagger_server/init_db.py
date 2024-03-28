import os
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="fisherman",
    user=os.environ["DB_USERNAME"],
    password=os.environ["DB_PASSWORD"],
    port="6666",
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table

# Insert data into the table

cur.execute(
    'INSERT INTO "Employee" ("employeeName", "birth", "address", "phone", "email", "positionID", "salary", "active")'
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
    (
        "Gina",
        "1997-04-07",
        "Address 88",
        "999-654-321",
        "gina@example.com",
        4,
        6000,
        True,
    ),
)


conn.commit()

cur.close()
conn.close()
