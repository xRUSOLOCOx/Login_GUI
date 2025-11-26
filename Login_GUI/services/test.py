import flet as ft
import time

def main(page: ft.Page):
    page.padding = 20

    # --- Banner simulado ---
    banner = ft.Container(
        visible=False,       # Oculto por defecto
        bgcolor=ft.Colors.GREEN_300,
        padding=15,
        border_radius=10,
        animate_opacity=300,
        opacity=0,
        content=ft.Row(
            [
                ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.AMBER, size=40),
                ft.Text(
                    "Oops, ocurrió un error eliminando el archivo.",
                    color=ft.Colors.BLACK,
                    expand=1
                ),
                ft.TextButton(text="salir",on_click=lambda e: hide_banner(e)),
                ft.TextButton("Ignore"),
                ft.TextButton("Cancel"),
            ],
            alignment="spaceBetween",
        ),
    )

    # --- Área principal donde quieres meter el banner ---
    main_container = ft.Column(
        [
            banner,
            ft.Text("Contenido principal debajo del banner"),
        ],
        spacing=20
    )

    # --- Funciones para mostrar / ocultar el banner ---
    def show_banner(e):
        banner.visible = True
        banner.opacity = 0
        banner.update()
        time.sleep(0.05)
        banner.opacity = 1
        banner.update()

    def hide_banner(e):
        banner.opacity = 0
        banner.update()
        time.sleep(0.2)
        banner.visible = False
        banner.update()

    # Botones para probar
    page.add(
        ft.Column(
            [
                ft.ElevatedButton("Mostrar Banner", on_click=show_banner),
                ft.ElevatedButton("Ocultar Banner", on_click=hide_banner),
                main_container
            ],
            spacing=20
        )
    )

ft.app(target=main)

# diccionmarip = {"hola":"holamundo"}

# print(diccionmarip["hola"])