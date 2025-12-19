import flet as ft
import time

def show_alert_banner(e,message,component):

    # Extraccion de referencia controles necesarios:


    banner = component.content.controls[1]
    print(banner)








    # container = e.control.parent.parent
    # column = e.control.parent.controls
    # banner = column[0]
    # banner_content = banner.content
    # banner_text = banner_content.controls[1].value

    # # Modificación de propiedades de control:

    # banner_content.controls[1].value = message
    # banner.bgcolor = "#F03636"
    # banner.visible = True
    # banner.opacity = 0
    # banner.update()

    # # Animar entrada del banner

    # time.sleep(0.1)
    # banner.opacity = 1
    # banner.update()

    # # Animar desplazamiento del contenedor hacia abajo

    # container.padding = ft.padding.only(top=10)
    # container.update()


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