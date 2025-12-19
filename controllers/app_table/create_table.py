import flet as ft
import time
from controllers.app_table import table_sentence
from controllers.app_context import app_context






def create_table():

    results = table_sentence.extract_users()
    rows = []

    if results:
          
        for row in results:

                rows.append(

                    ft.DataRow(

                        cells=[

                            ft.DataCell(ft.Text(row[0])),
                            ft.DataCell(ft.Text(row[1])),
                            ft.DataCell(ft.Text(row[2])),
                            ft.DataCell(ft.Text(row[3])),

                        ]
                    )
                )

        return ft.Container(

            content=ft.Column(
                 
                 [
                      


                    ft.DataTable(

                    columns=[

                        ft.DataColumn(ft.Text("ID",col="black")),
                        ft.DataColumn(ft.Text("NOMBRE",col="black")),
                        ft.DataColumn(ft.Text("EDAD",col="black"), numeric=True),
                        ft.DataColumn(ft.Text("CORREO",col="black")),

                    ],

                    rows=rows,
                    width=1000,
                    heading_row_color=ft.Colors.BLACK,
                    heading_row_height=48,
                    divider_thickness=0.8,
                    border=ft.border.all(0.5, ft.Colors.GREY_300),
                    horizontal_margin=12,
                    column_spacing=24,
                    
                    ),

                 ],

                 height=350,
                 scroll=ft.ScrollMode.ALWAYS

            ),

            
            
        )

    else:
         
        return False
    




