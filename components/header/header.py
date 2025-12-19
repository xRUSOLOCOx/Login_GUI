import flet as ft

                
def header_component(component_switcher):

    
    return ft.Container(

        content= ft.Row(

        [

            ft.Text(

                spans=[ft.TextSpan(text="LOGIN_GUI",on_click=component_switcher)],

                color="white",
                size=40,
                font_family=ft.FontWeight.BOLD

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

    )

