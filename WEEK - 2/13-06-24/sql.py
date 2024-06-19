import mysql.connector

# Establishing a connection to MySQL
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="testdb"  
    )

    if connection.is_connected():
        print("Connected to MySQL")

        # Inserting data into the 'users' table
        cursor = connection.cursor()
        insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        user_data = ("John Doe", "johndoe@example.com")
        cursor.execute(insert_query, user_data)
        connection.commit()
        print("Data inserted successfully")

        # Retrieving data from the 'users' table
        select_query = "SELECT * FROM users"
        cursor.execute(select_query)
        users = cursor.fetchall()
        for user in users:
            print(user)

except mysql.connector.Error as e:
    print("Error connecting to MySQL:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
