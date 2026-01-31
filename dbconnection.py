import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="buzodb"
        )
        if connection.is_connected():
            print("Connection to the database was successful.")
            return connection
    except Error as e:
        print("Error while connecting to MySQL:", e)
        return None