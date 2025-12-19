import re
from controllers.data_verification.show_banners import show_banners
from controllers.data_verification.hide_banners import hide_banners
from controllers.data_verification.sign_admin_in_verification.sign_admin_in_data import sign_admin_in_data
from controllers.data_verification.sign_admin_in_verification.sign_admin_in_errors import sign_admin_in_errors
from controllers.data_verification.sign_admin_in_verification.sign_admin_in_post import sign_admin_in_post

regular_expressions = {
        
    "email": r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
    "password": r"^(?=.*[A-Z])(?=.*\d)[A-Za-z\d@#$%^&+=!¡¿?._-]{8,}$",
        
}

def sign_admin_in_verification(e):

    # Obtencion de campos de registro:

    user_data = sign_admin_in_data.data_extraction(e)
    user_email = user_data["user_email"]
    user_password = user_data["user_password"]

    fields_validation = sign_admin_in_errors.sign_admin_in_error_fields(user_email,user_password)
    

    if fields_validation:

        errors_log = []
     
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

            sign_admin_in_post.sign_admin_in_post(e,user_email,user_password)