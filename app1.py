import mysql.connector
def connect_to_db():
    # Set up the connection details
    dbconnection = mysql.connector.connect(
        host="database",
        user="root",
        password="123",
        database="task4db"
    )
    return dbconnection

def read_write_data_from_db():
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        sql = "INSERT INTO emp1 (firstname, lastname) VALUES (%s, %s)"
        val = ("python_user", "pod_2")
        cursor.execute(sql, val)
        connection.commit()
        cursor.execute("SELECT * FROM emp1;")  # Change `your_table` to the actual table name
        results = cursor.fetchall()
        for row in results:
            print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    read_write_data_from_db()
