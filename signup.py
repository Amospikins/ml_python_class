from dbconnection import get_connection
def sign_up(fullname, email, password):
    connection = get_connection()
    
    if connection is None:
        print("Failed to connect to the database.")
        # return {"status": "error", "message": "Database connection failed"}

    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO user (fullname, email, password) 
            VALUES (%s, %s, %s)
            """
            
        cursor.execute(query, (fullname, email, password))
        connection.commit()
        print("User signed up successfully.")
    except Exception as e:
            print("Error during signup:", e)
    finally:
            cursor.close()
            connection.close()
    

