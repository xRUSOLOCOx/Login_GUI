import flet as ft
from controllers.app_navegation import app_navegation
from controllers.app_context import app_context


def sign_in_component():
        
        return ft.Container(
            
            
            content= ft.Column(

            [

                # Controles principales de componente sign in:

                ft.Text(value="INICIO DE SESIÓN USUARIO",size=30,weight=ft.FontWeight.BOLD),
                ft.TextField(label="Correo:",width=550,border_color="white"),
                ft.TextField(label="Contraseña:",width=550,border_color="white"),

                # Boton de envio de datos:

                ft.Button(text="ENTRAR",width=550,bgcolor="green",color="black",style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(10))),


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