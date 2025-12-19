from mysql.connector import Error
from services.password_crypt import password_crypt
import db_connection


def verify_user(cursor,user_email,user_password):
    
    try:

        verify_user_email = "SELECT user_password,user_email,user_id,user_age,user_name FROM users WHERE user_email = %s"
        cursor.execute(verify_user_email,(user_email,))
        is_user = cursor.fetchone()
        
        if not is_user:

            return False
        
        password_bytes = user_password.encode('utf-8')
        hashed_password = is_user[0].encode('utf-8')

        if password_crypt.verify_password(password_bytes,hashed_password):
        
            user_data = {

                "id":is_user[2],
                "role":"user",
                "email":is_user[1],
                "age":is_user[3],
                "name":is_user[4]

            }

            return user_data
        
        else:

            return False
    
    except:

        return False

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


def sign_in(user_email,user_password):

    try:

        connection = db_connection.database_connection()
        cursor = connection.cursor()
        
        verify_user_function = verify_user(cursor,user_email,user_password)
        

        if verify_user_function:
            return verify_user_function
        
        else:
            return "N/A"
        
    except:

        return False
        
    finally:

        connection.close()
        cursor.close()
