import flet as ft

from controllers.app_navegation import app_navegation
from controllers.app_context import app_context
from controllers.data_verification.hide_banners import hide_banners
from controllers.data_verification.sign_in_verification.sign_in_errors import sign_in_errors
from controllers.data_verification.sign_in_verification.sign_in_verification import sign_in_verification



def sign_in_component():
        
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


                ft.Text(
                        
                    value="INICIO DE SESIÓN USUARIO",
                    size=30,
                    weight=ft.FontWeight.BOLD
                    
                    ),

                ft.TextField(
                        
                    label="Correo:",
                    width=550,
                    border_color="white",
                    on_blur=lambda e: sign_in_errors.sign_in_errors(e)
                    
                    ),

                ft.TextField(
                        
                    label="Contraseña:",
                    width=550,
                    border_color="white",
                    password=True,
                    can_reveal_password=True,
                    on_blur=lambda e: sign_in_errors.sign_in_errors(e)
                    
                    ),
    
                # Boton de envio de datos:

                ft.Button(
                        
                    text="ENTRAR", 
                    width=550,bgcolor="green",
                    color="black",
                    style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(10)),
                    on_click=lambda e: sign_in_verification.sign_in_verification(e)
                    
                    
                    ),


                ft.Row(
                    
                    [
                        
                        ft.Text(
                                
                                spans=[ft.TextSpan(
                                        
                                        
                                    text="¿olvidaste tu contraseña?",
                                    
                                        
                                        
                                    )],
                                
                                    color="#09C1FF"
                                
                        ),


                        ft.Text(
                                
                                spans=[ft.TextSpan(
                                        
                                        text="¡Registrate Aqui!",
                                        
                                        on_click=lambda e: app_navegation.component_switcher(e,app_context.main_container) 
                                        
                                        )],
                                        
                                        color="#09C1FF")
                     
                     ],
                    
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                    
                    ),
  
            ],

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=25,
            height=600,
            
        ),

        padding=ft.padding.only(top=70),
        animate_opacity=300,
        data="sign_in_component"
        
                                                                             
        )