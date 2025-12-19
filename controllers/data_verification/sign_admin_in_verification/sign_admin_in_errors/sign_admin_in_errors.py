def sign_admin_in_errors(e):

    if not e.control.value:
            
        e.control.error_text = "¡Este campo no puede estar vacío!"
        
    else:

        e.control.error_text = None
        
    e.control.update()


def sign_admin_in_error_fields(user_email,user_password):

    errors_log = []

    if not user_email.value:

        user_email.error_text = "¡Este campo no puede estar vacío!"
        user_email.update()
        errors_log.append(1)

    if not user_password.value:

        user_password.error_text = "¡Este campo no puede estar vacío!"
        user_password.update()
        errors_log.append(1)

    if len(errors_log)>= 1:
        
        return False

    else:
        
        return True