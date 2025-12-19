import flet as ft

# COMPONENTES:

from components.header import header
from components.navegation import navegation
from components.content import content
from controllers.app_context import app_context

# CONTROLADORES:

from controllers.app_navegation import app_navegation

def main_component():

    content_component = content.content_component()
    app_context.main_container = content_component
    
    return ft.View(

        padding=0,
        route="/app",
        controls=[

            ft.Column(

            [
                
                header.header_component(lambda e: app_navegation.component_switcher(e,content_component)),

                ft.Container(

                    content=ft.Row(


                        [

                            ft.Container(

                                content=content_component,
                                expand=4,
                                border=ft.border.only(right=ft.BorderSide(1,"white")),
                                
                            ),


                            ft.Container(

                                content=navegation.nav_component(

                                    lambda e: app_navegation.component_switcher(e,content_component)

                                    ),

                                expand=1,
                                
                                
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