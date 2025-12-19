import time


from components.sign_up_modal import sign_up_modal
from controllers.app_context import app_context
from controllers.data_verification.show_banners import show_banners
from controllers.data_verification.sign_in_verification.sign_in_post import sign_in_sentences

from components.loading_components.app_loading import app_loading


def sign_in_post(e,user_email,user_password):


    data_post = sign_in_sentences.sign_in(
        
        str(user_email.value).strip(),
        str(user_password.value).strip()
    
    )

    if data_post == False:

        show_banners.show_alert_banner(e,"Error: Error de servidor")


    if isinstance(data_post, dict):

        if data_post["role"] == "user":

            # Extraccion de datos desde base de datos:

            user_id = data_post["id"]
            user_email = data_post["email"]
            user_age = data_post["age"]
            user_role = data_post["role"]
            user_name = data_post["name"]

            # Asignacion a variables globales:

            app_context.user_id = user_id
            app_context.user_email = user_email
            app_context.user_age = user_age
            app_context.user_role = user_role
            app_context.user_name = user_name


            app_context.page.open(app_loading.app_loading())
            time.sleep(5)

            app_context.page.go("/app")


    if data_post == "N/A":

        show_banners.show_alert_banner(e,"Error: Correo o Contraseña incorrecto.")

    