
from components.sign_up_modal import sign_up_modal
from controllers.app_context import app_context
from controllers.data_verification.show_banners import show_banners
from controllers.data_verification.sign_user_up_verification.sign_up_post import sign_up_sentences

def sign_up_post(e,user_name,user_age,user_email,user_password):


    data_post = sign_up_sentences.register_user(
        
        str(user_name.value).strip(),
        str(user_age.value).strip(),
        str(user_email.value).strip(),
        str(user_password.value).strip()
    
    )

    if data_post == False:

        show_banners.show_alert_banner(e,"Error: Error de servidor")

    if data_post == True:

        app_context.page.open(sign_up_modal.sign_up_modal())

    if data_post == "EX":

        show_banners.show_alert_banner(e,"Error: Correo ya registrado, Inicia Sesion.")

    