import flet as ft
from controllers.app_navegation import app_navegation
from controllers.app_context import app_context

def sign_up_modal():
    
    def sign_up_modal_controller(e):

        app_navegation.component_switcher(e,app_context.main_container)
        e.page.close(e.control.parent)


    return ft.AlertDialog(

        modal=True,
        title=ft.Text("Bienvenido, tu registro fue exitoso",color="green",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD),
        content=ft.Text("Continúa navegando o inicia sesión.",color="black",text_align=ft.TextAlign.CENTER,size=15,weight=ft.FontWeight.BOLD),
        actions=[

            ft.Button(
                    
                    text="Iniciar Sesion",
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),bgcolor="white",side=ft.BorderSide(width=1,color="green"),padding=ft.padding.only(top=20,bottom=20)),
                    color="green",
                    width=170,
                    on_click=lambda e: sign_up_modal_controller(e)
                    
               ),


                ft.Button(

                    text="Salir",
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),bgcolor="white",side=ft.BorderSide(width=1,color="red"),padding=ft.padding.only(top=20,bottom=20)),
                    color="red",
                    width=170,
                    on_click=lambda e: app_context.page.close(e.control.parent)
                
                ),

        ],

        actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        bgcolor="white",
        shape=ft.RoundedRectangleBorder(radius=9.0),
        icon=ft.Icon(name=ft.Icons.CHECK_ROUNDED, color="green", size=100),
        actions_padding=ft.padding.only(top=15,left=20,right=20,bottom=20)

    )




