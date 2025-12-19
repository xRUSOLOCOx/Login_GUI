from mysql.connector import Error
import db_connection


def extract_users():
    
    connection = db_connection.database_connection()
    cursor = connection.cursor()

    try:

        query = "SELECT user_id,user_name,user_age,user_email FROM users"
        cursor.execute(query)

        results = cursor.fetchall()
   
        return results
    
    except Error as e:

        return False

    finally:

        cursor.close()
        connection.close()
