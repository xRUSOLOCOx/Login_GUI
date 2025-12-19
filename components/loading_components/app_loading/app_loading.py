import flet as ft

def app_loading():

    return ft.AlertDialog(

            content=ft.CupertinoActivityIndicator(

                radius=50,
                color=ft.Colors.WHITE,

                animating=True,

            ),

            bgcolor=ft.Colors.TRANSPARENT,
            modal= True

        )


