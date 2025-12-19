import flet as ft
from components.app.profile_menu import profile_menu
from controllers.app_context import app_context

def header_component():

    return ft.Container(

        content= ft.Row(

        [

            ft.Text(

                color="white",
                size=40,
                font_family=ft.FontWeight.BOLD,
                value="LOGIN_GUI"

            ),

        
            ft.Row(


                [

                    ft.Text(
                        
                        value=f"{app_context.user_name}"
                        
                        
                    ),


                    profile_menu.profile_menu()

                ]

            )
              
        ],

        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        
    ),

    padding=ft.padding.only(left=10,right=10),
    border=ft.border.only(bottom=ft.BorderSide(1,"white")),
    bgcolor="#11212d"

    )