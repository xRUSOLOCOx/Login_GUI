from time import sleep
import flet as ft


def loading_bar():

    return ft.View(

        route="/loading",
        controls=[

            ft.Column(controls=[


                ft.Container(

                    content= ft.Row(

                    [

                        ft.Text(

                            color="white",
                            size=40,
                            font_family=ft.FontWeight.BOLD,
                            value="LOGIN_GUI"

                        ),


                        ft.Image(
                
                        src=r"Login_GUI\assets\icons\icon.jpg",
                        width=80,
                        height=80
                
                        )


                    ],

                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    
                ),

                padding=ft.padding.only(left=10,right=10),
                border=ft.border.only(bottom=ft.BorderSide(1,"white")),
                bgcolor="#11212d"

                ),

                ft.Container(

                    content=ft.Column(



                        controls=[

                            ft.Text("Cargado Aplicacion", style=ft.TextThemeStyle.HEADLINE_SMALL,text_align=ft.TextAlign.CENTER),
                            ft.ProgressBar(width=600, color=ft.Colors.BLUE, bgcolor="#eeeeee"),

                        ],

                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20

                    ),

                    margin=ft.margin.only(top=200)

                )

            ],

            spacing=30,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            )

        ]
        ,

        horizontal_alignment= ft.CrossAxisAlignment.CENTER,
        padding=0,
        

    )




        



    

   


    