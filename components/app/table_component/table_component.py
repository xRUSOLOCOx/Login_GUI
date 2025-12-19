import flet as ft
from controllers.app_table import table_sentence
from controllers.app_table import create_table
from controllers.app_context import app_context

from controllers.app_load import app_load



def table_component():

    return ft.Container(

        content=ft.Column(

            [

                ft.Container(

                    content=ft.Text(value="USUARIOS REGISTRADOS EN EL SISTEMA LOGIN_GUI",size=25,weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER),
                    alignment=ft.alignment.center
                    
                ),

                ft.Button(
                    
                    text="Actualizar",
                    width=200,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),bgcolor="white",side=ft.BorderSide(width=1,color="blue"),padding=ft.padding.only(top=20,bottom=20)),
                    color="blue",
                    on_click= lambda e: app_load.update_table(e)
                    
                    ),

                app_context.users

            ],

            spacing=30,
            
        ),

        padding=ft.padding.only(left=10,top=10,right=20),

        data="table_component"

    )