import re
import flet as ft
from controllers.data_verification.show_banners import show_banners
from controllers.data_verification.hide_banners import hide_banners
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
    
    # Verificación y asignacion de capmpos de texto:
    
    if sign_up_errors.sign_up_error_fields(user_name,user_age,user_email,user_password):

        errors_log = []

        if not re.fullmatch(regular_expressions["name"],str(user_name.value).strip()):

            errors_log.append("Error Nombre: Solo letras (acepta acentos) 10 a 60 caracteres.")
           

        if not re.fullmatch(regular_expressions["age"],str(user_age.value).strip()):

            errors_log.append("Error Edad: Solo número entero entre 0 y 120")
            

        if not re.fullmatch(regular_expressions["email"],str(user_email.value).strip()):

            errors_log.append("Error Correo: Ha ingresado un correo invalido")
            

        if not re.fullmatch(regular_expressions["password"],str(user_password.value).strip()):

            errors_log.append("Error Contraseña: Minimo 8 caracteres; una MAYÚSCULA , al menos un dígito y un simbolo")
            
        if len(errors_log)>= 1:
            
            show_banners.show_alert_banner(e,errors_log[0])
            errors_log.clear()

        # Envio de datos:
        
        else:
            
            banner_element = e.control.parent.controls[0]
            
            if banner_element.opacity == 1:
            
                hide_banners.hide_alert_banner(e)
                
            
            else:
                
                pass
