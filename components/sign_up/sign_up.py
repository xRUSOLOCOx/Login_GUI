import flet as ft
from controllers.app_navegation import app_navegation
from controllers.app_context import app_context
from controllers.data_verification.sign_user_up_verification.sign_up_verification import sign_up_verification
from controllers.data_verification.sign_user_up_verification.sign_up_errors import sign_up_errors
from controllers.data_verification.hide_banners import hide_banners

main_container = app_context.main_container

def sign_up_component():
        
        return ft.Container(
            
            content= ft.Column(

            [

                ft.Container(
                        
                        visible=False,       
                        padding=0,
                        border_radius=10,
                        animate_opacity=300,
                        animate_offset=300,
                        opacity=0,
                        bgcolor ="",

                        content=ft.Row(
                                
                            [
                                ft.Icon(
                                        
                                    ft.Icons.WARNING_AMBER_ROUNDED, 
                                    color=ft.Colors.WHITE, 
                                    size=40
                                    
                                    ),

                                ft.Text(

                                    value ="",
                                    color=ft.Colors.WHITE,
                                    expand=1,
                                    weight=ft.FontWeight.NORMAL
                                ),

                                ft.TextButton(
                                    
                                    text="SALIR",
                                    on_click=lambda e:hide_banners.hide_alert_banner(e),
                                    style=ft.ButtonStyle(color="white")
                                    ),
    
                            ],

                        alignment="spaceBetween",
                        width=550

                    ),
                ),



                ft.Text(value="CREA TU CUENTA USUARIO",size=30,weight=ft.FontWeight.BOLD),
                

                ft.Row(

                    
                    [
                        
                        ft.TextField(
                                
                            label="Nombre Completo:",
                            border_color="white",
                            width=265,
                            on_blur=lambda e: sign_up_errors.sign_up_errors(e)
                                
                        ),

                        ft.TextField(
                                
                            label="Edad:",
                            border_color="white",
                            width=265,
                            on_blur=lambda e: sign_up_errors.sign_up_errors(e)
                            
                            ),
                            
                     ],
                    
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20

                

                ),


                ft.TextField(
                        
                        label="Correo:",
                        width=550,
                        border_color="white",
                        on_blur=lambda e: sign_up_errors.sign_up_errors(e)

                        ),

                ft.TextField(
                        
                        label="Contraseña:",
                        width=550,
                        border_color="white",
                        on_blur=lambda e: sign_up_errors.sign_up_errors(e),
                        password=True,
                        can_reveal_password=True

                        ),


                # Boton de envio de datos:

                ft.Button(
                    
                    text="ENTRAR",
                    width=550,
                    bgcolor="green",
                    color="black",
                    style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(10)),
                    on_click=lambda e: sign_up_verification.sign_up_verification(e)
                    
                    
                    ),
                    

                ft.Row(
                    
                    [
                        
                        ft.Text(
                                
                                spans=[ft.TextSpan(
                                        
                                        text="¿Ya tienes cuenta?",
                                        
                                        on_click= lambda e: app_navegation.component_switcher(e,app_context.main_container)
                                        
                                        
                                        )
                                        
                                    ],
                                    
                                color="#09C1FF"
                                
                                
                        ),

                        ft.Text(
                                
                                spans=[ft.TextSpan(text="Terminos y condiciones")],color="#09C1FF"
                                
                        )
                     
                     ],
                    
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                    
                    ),
  
            ],

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=25,
            height=600,
            
        ),

        padding=ft.padding.only(top=60),
        data="sign_up_component",
        animate_offset=300
        
        )