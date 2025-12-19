import re
import flet as ft
from controllers.data_verification.show_banners import show_banners
from controllers.data_verification.hide_banners import hide_banners
from controllers.data_verification.sign_user_up_verification.sign_up_data import sign_up_data
from controllers.data_verification.sign_user_up_verification.sign_up_errors import sign_up_errors
from controllers.data_verification.sign_user_up_verification.sign_up_post import sign_up_post



regular_expressions = {
        
    "name": r"^[A-Za-zÀ-ÖØ-öø-ÿ' \-]{10,60}$",
    "age": r"^(?:1[89]|[2-9]\d|1[01]\d|120)$",
    "email": r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
    "password": r"^(?=.*[A-Z])(?=.*\d)[A-Za-z\d@#$%^&+=!¡¿?._-]{8,}$",
        
}


def sign_up_verification(e):

    # Obtencion de campos de registro:

    user_data = sign_up_data.data_extraction(e)
    user_name = user_data["user_name"]
    user_age =  user_data["user_age"]
    user_email = user_data["user_email"]
    user_password = user_data["user_password"]

    fields_validation = sign_up_errors.sign_up_error_fields(user_name,user_age,user_email,user_password)
    

    if fields_validation:

        errors_log = []

        if not re.fullmatch(regular_expressions["name"],str(user_name.value).strip()):
            errors_log.append("Error Nombre: Solo letras (acepta acentos) 10 a 60 caracteres.")
            
        if not re.fullmatch(regular_expressions["age"],str(user_age.value).strip()):
            errors_log.append("Error Edad: Solo número entero entre 18 y 120")
                
        if not re.fullmatch(regular_expressions["email"],str(user_email.value).strip()):
            errors_log.append("Error Correo: Ha ingresado un correo invalido")
                
        if not re.fullmatch(regular_expressions["password"],str(user_password.value).strip()):
            errors_log.append("Error Contraseña: Minimo 8 caracteres; una MAYÚSCULA , al menos un dígito y un simbolo")


        if len(errors_log)>= 1:
                
            show_banners.show_alert_banner(e,errors_log[0])
            errors_log.clear()

        else:

            banner_status = e.control.parent.controls[0].opacity
            
            if banner_status != 0:

                hide_banners.hide_alert_banner(e)

            # llamada a funcion de envio a base de datos:

            sign_up_post.sign_up_post(e,user_name,user_age,user_email,user_password)


            
