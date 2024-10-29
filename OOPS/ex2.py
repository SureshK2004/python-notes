import mysql.connector
from mysql.connector import Error


class MySQLDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user  
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error: {e}")

    def create_table(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            print("Table created successfully")
        except Error as e:
            print(f"Error: {e}")

    def insert_record(self, query, values):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            print("Record inserted successfully")
        except Error as e:
            print(f"Error: {e}")

    def query_records(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except Error as e:
            print(f"Error: {e}")
            return None

    def update_record(self, query, values):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            print("Record updated successfully")
        except Error as e:
            print(f"Error: {e}")

    def delete_record(self, query, values):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            print("Record deleted successfully")
        except Error as e:
            print(f"Error: {e}")

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Connection closed")
# Usage example
if __name__ == "__main__":
    db = MySQLDatabase(host='localhost', user='root', password='suresh', database='test_db')

    db.connect()

    create_table_query = """ 
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        salary DECIMAL(10, 2) NOT NULL
    )
    """
    db.create_table(create_table_query)
    insert_query = "INSERT INTO employees (name, salary) VALUES (%s, %s)"
    db.insert_record(insert_query, ('John Doe', 50000))

    select_query = "SELECT * FROM employees"
    records = db.query_records(select_query)
    print("All records:", records)

    update_query = "UPDATE employees SET salary = %s WHERE name = %s"
    db.update_record(update_query, (60000, 'John Doe'))

    records = db.query_records(select_query)
    print("Records after update:", records)

    delete_query = "DELETE FROM employees WHERE name = %s"
    db.delete_record(delete_query, ('John Doe',))

    records = db.query_records(select_query)
    print("Records after deletion:", records)

    db.close()