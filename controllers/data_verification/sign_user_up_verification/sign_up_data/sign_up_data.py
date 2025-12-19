def data_extraction(e):

    column = e.control.parent.controls

    # Campos de ingreso de datos de registro:

    user_name = column[2].controls[0]
    user_age = column[2].controls[1]
    user_email = column[3]
    user_password = column[4]

    # Retorno de campos estructurados:

    data_json = {
        
        "user_name":user_name,
        "user_age":user_age,
        "user_email":user_email,
        "user_password":user_password
        
    }

    return data_json