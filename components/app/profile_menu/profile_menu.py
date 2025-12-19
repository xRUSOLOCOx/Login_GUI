import flet as ft
from controllers.app_context import app_context
from components.app.log_out_modal import log_out_modal


def profile_menu():

    page = app_context.page

    return ft.PopupMenuButton(

        bgcolor=ft.Colors.WHITE,
        items=[

            
            
            ft.PopupMenuItem(

                content=ft.Row(

                    [
                        ft.Icon(ft.Icons.PERSON, color=ft.Colors.BLACK),
                        ft.Text("Perfil", color=ft.Colors.BLACK),
                    ]
                ),

                disabled=True
            ),

            ft.PopupMenuItem(

                content=ft.Text(

                    f"id: {app_context.user_id}",
                    color=ft.Colors.BLACK
                ),

                disabled=True
            ),

            ft.PopupMenuItem(

                content=ft.Text(

                    f"{app_context.user_name}",
                    color=ft.Colors.BLACK
                ),

                disabled=True
            ),

            ft.PopupMenuItem(

                content=ft.Text(

                    f"{app_context.user_age} años",
                    color=ft.Colors.BLACK

                ),
                disabled=True
            ),

            ft.PopupMenuItem(

                content=ft.Text(

                    f"{app_context.user_email}",
                    color=ft.Colors.BLACK

                ),

                disabled=True
            ),

            ft.PopupMenuItem(

                content=ft.Text(

                    f"rol: {app_context.user_role}",
                    color=ft.Colors.BLACK
                ),

                disabled=True
            ),

            ft.PopupMenuItem(),  
            ft.PopupMenuItem(

                content=ft.Row(

                    [

                        ft.TextButton(
                            
                            text="Log Out",
                            col=ft.Colors.RED,
                            on_click= lambda e: page.open(log_out_modal.log_out_modal(e,page)),
                            icon=ft.Icons.LOGOUT,
                            icon_color=ft.Colors.RED,
                            style=ft.ButtonStyle(color=ft.Colors.RED)
                    
                            
                        )
                    ]
                ),
                
            ),
        ],

        icon=ft.Icons.PERSON,
        icon_color="white",
        icon_size=60
    )
