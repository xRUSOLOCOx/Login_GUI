def data_extraction(e):

    column = e.control.parent.controls

    # Campos de ingreso de datos de registro:

    user_email = column[2]
    user_password = column[3]

    # Retorno de campos estructurados:

    data_json = {
        
        "user_email":user_email,
        "user_password":user_password
        
    }

    return data_json