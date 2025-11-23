import flet as ft

def nav_component(component_switcher):
        
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
                    
                    

                    ),

                ft.Button(

                    text="Sign User Up",
                    width=400,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),bgcolor="white",side=ft.BorderSide(width=1,color="blue"),padding=ft.padding.only(top=20,bottom=20)),
                    color="blue",
                    


                    ),

                ft.Container(


                    content= ft.Button(

                    text="Quit System",
                    width=400,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),bgcolor="white",side=ft.BorderSide(width=1,color="red"),padding=ft.padding.only(top=20,bottom=20)),
                    color="red",
                    

                    ),

                    margin=ft.margin.only(top=150),
                    
                )

            ],

            spacing=50,   
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,


        ),

        padding=ft.padding.only(left=10,top=40,right=20)

        )