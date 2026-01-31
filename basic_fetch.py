import mysql.connector
from mysql.connector import Error

def fetch_users():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="buzodb"
        )
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM user")
            
            users = cursor.fetchall()
            return users
    except Error as e:
        print("Error while connecting to MySQL:", e)
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    



