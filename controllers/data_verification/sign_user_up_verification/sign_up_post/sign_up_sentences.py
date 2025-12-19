from mysql.connector import Error
from services.password_crypt import password_crypt
import db_connection


def register_user(user_name,user_age,user_email,user_password):

    try:

        # Conexion y cursor:

        connection = db_connection.database_connection()
        cursor = connection.cursor()

        # Consultas a base de datos:

        verify_email = "SELECT * FROM users WHERE user_email = %s"
        add_user = "INSERT INTO users (user_name,user_age,user_email,user_password) VALUES (%s,%s,%s,%s)"

        # Ejecutar consulta para verificar si el correo ya existe:

        cursor.execute(verify_email, (user_email,))
        existing = cursor.fetchone()

        if existing:

            return "EX"
        
        # Encriptación de contraseña:

        password_bytes = user_password.encode('utf-8')
        hashed_password = password_crypt.hash_password(password_bytes)

        # Ejecutar consulta de ingreso de datos:

        cursor.execute(add_user, (user_name, user_age, user_email, hashed_password))
        connection.commit()

        return True

    except Error as error:

        return False
    
    finally:

        connection.close()
        cursor.close()
