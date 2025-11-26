import flet as ft
import time

def show_alert_banner(e,message):

    # Extraccion de referencia controles necesarios:

    container = e.control.parent.parent
    column = e.control.parent.controls
    banner = column[0]
    banner_content = banner.content
    banner_text = banner_content.controls[1].value

    # Modificación de propiedades de control:

    banner_content.controls[1].value = message
    banner.bgcolor = "#E8DC9E"
    banner.visible = True
    banner.opacity = 0
    banner.update()

    # Animar entrada del banner

    time.sleep(0.1)
    banner.opacity = 1
    banner.update()

    # Animar desplazamiento del contenedor hacia abajo

    container.padding = ft.padding.only(top=10)
    container.update()