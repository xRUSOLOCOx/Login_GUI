import flet as ft
import time

def hide_alert_banner(e):
    
    if e.control.text == "SALIR":

        container = e.control.parent.parent.parent
        banner = e.control.parent.parent

    else:    
    
        container = e.control.parent.parent
        column = e.control.parent.controls
        banner = column[0]

    # Modificación de propiedades de control:

    banner.visible = True
    banner.opacity = 1
    banner.update()

    # Animar salida del banner

    time.sleep(0.1)
    banner.opacity = 0
    banner.update()

    # Animar desplazamiento del contenedor hacia abajo

    container.padding = ft.padding.only(top=10)
    container.update()