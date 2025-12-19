import flet as ft

def log_out_modal(e,page):

    dlg_modal = ft.AlertDialog(

        modal=True,
        title=ft.Text("Alerta de sistema"),
        content=ft.Text("¿Quires Cerrar sesión?"),

        actions=[

            ft.TextButton("Yes", on_click=lambda _: page.go("/")),
            ft.TextButton("No", on_click=lambda e: page.close(dlg_modal)),

        ],

        actions_alignment=ft.MainAxisAlignment.END,
        
    )


    return dlg_modal