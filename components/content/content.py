import flet as ft
from config import PROJECT_INSTRUCTIONS, PROJECT_INTRODUCTION
from controllers.text_transform import text_transform


def content_component():

        return ft.Container(

            content=ft.Column(

            [

                ft.Container(


                    content = ft.Column(
                        
                        [

                            ft.Text(value="PROYECTO LOGIN_GUI",size=25,weight=ft.FontWeight.BOLD),
                            ft.Text(value=text_transform.text_transform(PROJECT_INTRODUCTION),size=18,text_align=ft.TextAlign.JUSTIFY),

                        ]
                    
                    )

                ),

                ft.Container(


                    content=ft.Column(


                        [

                            ft.Text(value="INSTRUCCIONES",size=25,weight=ft.FontWeight.BOLD),
                            ft.Text(value=PROJECT_INSTRUCTIONS,size=18,text_align=ft.TextAlign.JUSTIFY),

                        ]
                    )
                )

                
            ],

            spacing=40,
            
            

        ),

        padding=ft.padding.only(left=10,top=40,right=20),
        animate_opacity=300,
        data="content_component"
        
        
        )