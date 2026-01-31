from dbconnection import get_connection
def user_login(email, password):
    connection = get_connection()
    
    if connection is None:
        print("Failed to connect to the database.")
    try:
        cursor = connection.cursor()
        query = """
            SELECT * FROM user 
            WHERE email = %s AND password = %s
            """
            
        cursor.execute(query, (email, password))
        user = cursor.fetchone()
        
        if user:
            print("Login successful.")
            
        else:
            print("Invalid email or password.")
           
    except Exception as e:
            print("Error during login:", e)
           
    finally:
            cursor.close()
            connection.close()