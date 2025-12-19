import flet as ft
from config import APP_PROJECT_INTRODUCTION, APP_PROJECT_INSTRUCTIONS
from controllers.text_transform import text_transform


def content_component():

        return ft.Container(

            content=ft.Column(

            [

                ft.Container(


                    content = ft.Column(
                        
                        [

                            ft.Text(value="APP LOGIN_GUI",size=25,weight=ft.FontWeight.BOLD),
                            ft.Text(value=text_transform.text_transform(APP_PROJECT_INTRODUCTION),size=18,text_align=ft.TextAlign.JUSTIFY),

                        ]
                    
                    )

                ),

                ft.Container(


                    content=ft.Column(


                        [

                            ft.Text(value="INSTRUCCIONES",size=25,weight=ft.FontWeight.BOLD),
                            ft.Text(value=APP_PROJECT_INSTRUCTIONS,size=18,text_align=ft.TextAlign.JUSTIFY),

                        ]
                    )
                )

                
            ],

            spacing=40,
            scroll=ft.ScrollMode.ALWAYS,
            height=550
            

        ),

        padding=ft.padding.only(left=10,top=40,right=20),
        animate_opacity=300,
        data="content_app_component"
        
        
        )