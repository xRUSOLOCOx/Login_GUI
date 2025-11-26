import re
import flet as ft
from controllers.data_verification.show_banners import show_banners
from controllers.data_verification.sign_up_errors import sign_up_errors


regular_expressions = {
        
    "name": r"^[A-Za-zÀ-ÖØ-öø-ÿ' \-]{10,60}$",
    "age": r"^(?:120|11[0-9]|10[0-9]|[1-9]?[0-9])$",
    "email": r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
    "password": r"^(?=.*[A-Z])(?=.*\d)[A-Za-z\d@#$%^&+=!¡¿?._-]{8,}$",
        
}

def sign_up_verification(e):

    # Extraer referencia de columna donde se almacenan los campos de texto del formulario:

    column = e.control.parent.controls

    # Campos de ingreso de datos de registro.

    user_name = column[2].controls[0]
    user_age = column[2].controls[1]
    user_email = column[3]
    user_password = column[4]
    
    if sign_up_errors.sign_up_error_fields(user_name,user_age,user_email,user_password):


        errors_log = []

        if not re.fullmatch(regular_expressions["name"],str(user_name.value)):
            errors_log.append("Error Nombre: Solo letras (acepta acentos) 10 a 60 caracteres.")



        if not re.fullmatch(regular_expressions["age"],str(user_age.value)):
            errors_log.append("Error en la edad")



        if not re.fullmatch(regular_expressions["email"],str(user_email.value)):
            errors_log.append("Error en el email")



        if not re.fullmatch(regular_expressions["password"],str(user_password.value)):
            errors_log.append("Error en la contraseña")


        if len(errors_log)>= 1:
            
            show_banners.show_alert_banner(e,errors_log[0])
            errors_log.clear()

        else:
            
            print(user_name.value,user_email.value,user_age.value,user_password.value)
