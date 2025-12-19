import flet as ft
from controllers.app_context import app_context
from controllers.quit_app import quit_app
from controllers.app_load import app_load

def nav_component(component_switcher):
        
        # Variable global page reutilizable

        page = app_context.page

        return ft.Container(


            content=ft.Column(

            [

                ft.Button(
                    
                    text="Sign User In",
                    width=400,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),bgcolor="white",side=ft.BorderSide(width=1,color="green"),padding=ft.padding.only(top=20,bottom=20)),
                    color="green",
                    on_click=component_switcher
                    
                    ),


                ft.Button(

                    text="Sign Admin In",
                    width=400,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),bgcolor="white",side=ft.BorderSide(width=1,color="green"),padding=ft.padding.only(top=20,bottom=20)),
                    color="green",
                    on_click=component_switcher
                    
                    

                    ),

                ft.Button(

                    text="Sign User Up",
                    width=400,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),bgcolor="white",side=ft.BorderSide(width=1,color="blue"),padding=ft.padding.only(top=20,bottom=20)),
                    color="blue",
                    on_click=component_switcher,


                    ),

                ft.Container(


                    content= ft.Button(

                    text="Quit System",
                    width=400,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),bgcolor="white",side=ft.BorderSide(width=1,color="red"),padding=ft.padding.only(top=20,bottom=20)),
                    color="red",
                    on_click=lambda e: quit_app.quit_app(e,page),

                    ),

                    margin=ft.margin.only(top=150),
                    
                )

            ],

            spacing=50,   
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,


        ),

        padding=ft.padding.only(left=10,top=40,right=20)

        )