import flet as ft
from controllers.app_context import app_context
from controllers.app_navegation import app_navegation

def admin_button_component(component_switcher):
        
    # Variable global page reutilizable

    page = app_context.page

    return ft.OutlinedButton(
                        
        width=300,

        style=ft.ButtonStyle(
                            
            shape=ft.RoundedRectangleBorder(radius=5),
            bgcolor=ft.Colors.WHITE,
            padding=ft.padding.only(top=20, bottom=20),
            color=ft.Colors.BLACK,
            side=ft.BorderSide(1,"black")

        ),

        content=ft.Row(
                            
            [   
                ft.Icon(name=ft.Icons.PEOPLE_ALT_SHARP,col="black",size=30),
                ft.Text(value="Users",col="black",size=15),
            ],

            alignment=ft.MainAxisAlignment.CENTER
        ),

        on_click=component_switcher

    )
