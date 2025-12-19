import flet as ft
from controllers.app_context import app_context
from components.app.admin import admin_components
from components.app.log_out_modal import log_out_modal


def nav_component(component_switcher):
        
        # Variable global page reutilizable

        page = app_context.page
        

        controls = [

            ft.OutlinedButton(
                        
                width=300,

                style=ft.ButtonStyle(
                            
                    shape=ft.RoundedRectangleBorder(radius=5),
                    bgcolor=ft.Colors.WHITE,
                    padding=ft.padding.only(top=20, bottom=20),
                    color=ft.Colors.BLACK,
                    side=ft.BorderSide(1,"black")
                ),

                content=ft.Row(
                            
                    [   
                        ft.Icon(name=ft.Icons.HOME_SHARP,col="black",size=30),
                        ft.Text(value="Home",col="black",size=15),
                    ],

                    alignment=ft.MainAxisAlignment.CENTER
                ),

                on_click= component_switcher
                
            ),

        ]

        if app_context.user_role == "admin":

            controls.insert(1, admin_components.admin_button_component(component_switcher))
            margin_top = 250

        else:

            margin_top = 350

        controls.append(

            ft.Container(
                        
                content=ft.OutlinedButton(
                        
                    width=300,

                    style=ft.ButtonStyle(
                                
                        shape=ft.RoundedRectangleBorder(radius=5),
                        bgcolor=ft.Colors.WHITE,
                        padding=ft.padding.only(top=20, bottom=20),
                        color=ft.Colors.RED,
                        side=ft.BorderSide(1,"red")
                    ),

                    content=ft.Row(
                                
                        [   
                            ft.Icon(name=ft.Icons.EXIT_TO_APP,col="red",size=30),
                            ft.Text(value="Log Out",col=ft.Colors.RED,size=15),
                        ],

                        alignment=ft.MainAxisAlignment.CENTER
                    ),

                    on_click=lambda e: page.open(log_out_modal.log_out_modal(e,page))
                
                ),
                margin=ft.margin.only(top=margin_top)

            )

        )
        
        return ft.Container(
             
            content=ft.Column(

                controls,

                spacing=50,   
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),

            padding=ft.padding.only(left=10,top=40,right=20)

        )