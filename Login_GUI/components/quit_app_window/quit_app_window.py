import flet as ft


def quit_app_window(page):



    dlg_modal = ft.AlertDialog(

        modal=True,
        title=ft.Text("Alerta de sistema"),
        content=ft.Text("¿Quires cerrar la aplicación?"),

        actions=[

            ft.TextButton("Yes", on_click=lambda e: page.window.destroy()),
            ft.TextButton("No", on_click=lambda e: page.close(dlg_modal)),

        ],

        actions_alignment=ft.MainAxisAlignment.END,
        
    )


    return dlg_modal



    # page.add(

    #     ft.ElevatedButton("Open modal dialog", on_click=lambda e: page.open(dlg_modal)),

    # )

