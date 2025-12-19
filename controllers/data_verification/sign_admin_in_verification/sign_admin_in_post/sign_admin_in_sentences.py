from mysql.connector import Error
from services.password_crypt import password_crypt
import db_connection


def verify_admin(cursor,user_email,user_password):
    
    try:

        verify_admin_email = "SELECT admin_password,admin_email,admin_id,admin_age,admin_name FROM admins WHERE admin_email = %s"
        cursor.execute(verify_admin_email,(user_email,))
        is_admin = cursor.fetchone()
        
        if not is_admin:

            return False
        
        password_bytes = user_password.encode('utf-8')
        hashed_password = is_admin[0].encode('utf-8')

        if password_crypt.verify_password(password_bytes,hashed_password):


            admin_data = {

                "id":is_admin[2],
                "role":"admin",
                "email":is_admin[1],
                "age":is_admin[3],
                "name":is_admin[4],

            }

            return admin_data
        
        else:

            return False
    
    except:

        return False


def sign_admin_in(user_email,user_password):

    try:

        connection = db_connection.database_connection()
        cursor = connection.cursor()
        
        verify_admin_function = verify_admin(cursor,user_email,user_password)
        

        if verify_admin_function:
            return verify_admin_function
        
        if not verify_admin_function:
            return "N/A"
        
    except:

        return False
        
    finally:

        connection.close()
        cursor.close()