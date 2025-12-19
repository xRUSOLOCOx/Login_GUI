import flet as ft

# COMPONENTES:

from components.app.app_header import app_header
from components.app.app_navegation import app_navegation_component
from components.app.app_content import app_content
from components.app.table_component import table_component
from controllers.app_context import app_context


# CONTROLADORES:

from controllers.app_navegation import app_navegation

def main_component():

    content_component = app_content.content_component()
    

    return ft.View(


        padding=0,
        route="/",
        controls=[

            ft.Column(

            [
                
                app_header.header_component(),

                ft.Container(

                    content=ft.Row(


                        [

                            ft.Container(

                                content=app_navegation_component.nav_component(

                                    lambda e: app_navegation.app_component_switcher(e,content_component)

                                ),

                                expand=1,
                                border=ft.border.only(right=ft.BorderSide(1,"white")),
                                height=700
                            ),


                            ft.Container(

                                content=content_component,
                                expand=4,
                                
                                
                            )

                        ],

                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.START


                    )

                )
  
            ],

            spacing=0
            
            
        )


        ]

    )





        
    