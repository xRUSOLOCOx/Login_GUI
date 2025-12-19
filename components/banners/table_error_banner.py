import flet as ft

def table_error_table():


    return ft.Container(
                                   
        padding=0,
        border_radius=10,
        bgcolor ="red",
        content=ft.Row(
                                    
            [
                ft.Icon(
                                            
                    ft.Icons.WARNING_AMBER_ROUNDED, 
                    color=ft.Colors.WHITE, 
                    size=40
                                        
                ),

                ft.Text(

                    value ="Error de servidor: No se ha podido cargar la tabla",
                    color=ft.Colors.WHITE,
                    expand=1,
                    weight=ft.FontWeight.NORMAL,
                    size=20
                    

                ),

                ],

                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                width=550,
                height=300,
                scroll=ft.ScrollMode.ALWAYS,

        ),

        alignment=ft.alignment.center
    )