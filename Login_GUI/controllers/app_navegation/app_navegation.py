import time

from components.content import content
from components.sign_in import sign_in



def component_switcher(e,main_component):

    sign_in_component = sign_in.sign_in_component()

    

    
    if e.control.text == "Sign User In":


        if main_component.data != "sign_in_component":
            print(main_component.data,"soy data")






            main_component.opacity = 0
            main_component.update()
            time.sleep(0.2)

            main_component.content = sign_in_component
            main_component.data = "sign_in_component"
            main_component.update()

            time.sleep(0.2)  
            main_component.opacity = 1
            main_component.update()

            print(sign_in_component.data)

        else:
            return



    