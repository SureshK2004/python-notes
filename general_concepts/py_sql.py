import pymysql

# Replace these with your actual database credentials
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'Host',
    'password': 'suresh',
    'database': 'besant'
}

cnx = None

try:
    # Establish the connection
    cnx = pymysql.connect(**config)

    print("Successfully connected to the database")

    # Create a cursor object
    cursor = cnx.cursor()

    # Sample query to show databases
    cursor.execute("SHOW DATABASES")

    # Fetch and print all databases
    for (database,) in cursor:
        print(database)

    # Close the cursor
    cursor.close()

except pymysql.MySQLError as e:
    print(f"Error: {e}")

finally:
    # Ensure the connection is closed
    if cnx:
        cnx.close()
        print("Database connection closed")
