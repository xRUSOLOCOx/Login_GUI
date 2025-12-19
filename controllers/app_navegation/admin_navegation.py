# CONTROLADOR DE MANEJO DE NAVEGACION LOGIN_GUI:


import time

from components.content import content
from components.sign_in import sign_in
from components.sign_up import sign_up

def opacity_animation(main_component,new_component,data):

    main_component.opacity = 0
    main_component.update()
    time.sleep(0.3)

    main_component.content = new_component
    main_component.data = data
    main_component.update()

    time.sleep(0.3)  
    main_component.opacity = 1
    main_component.update()


def jump_animation():
    pass


def component_switcher(e,main_component):

    sign_in_component = sign_in.sign_in_component()
    content_component = content.content_component()
    sign_up_component = sign_up.sign_up_component()


    if e.control.text in ("Sign User In","¿Ya tienes cuenta?","Iniciar Sesion"):

        if main_component.data != "sign_in_component":
            opacity_animation(main_component,sign_in_component,"sign_in_component")


    if e.control.text == "LOGIN_GUI":

        if main_component.data != "content_component":
            opacity_animation(main_component,content_component.content,"content_component")

    if e.control.text in ("Sign User Up","¡Registrate Aqui!"):

        print("presionada")

        if main_component.data != "sign_up_component":
            opacity_animation(main_component,sign_up_component,"sign_up_component")



def app_component_switcher():
    pass