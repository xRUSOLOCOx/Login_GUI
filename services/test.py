from time import sleep
# import flet as ft


# def main(page):
#     page.theme_mode = ft.ThemeMode.LIGHT

#     page.add(
#         ft.CupertinoActivityIndicator(
#             radius=50,
#             color=ft.Colors.RED,
#             animating=True,
#         )
#     )


# ft.app(main)


import flet as ft


def main(page: ft.Page):

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ALWAYS
    pb = ft.ProgressBar(width=400)



    page.add(

        ft.FilledButton(

            text="Open Material Dialog",
            on_click=lambda e: page.open(

                ft.AlertDialog(

                    content=pb,
                    bgcolor=ft.Colors.TRANSPARENT,
                    modal= True


                )
            ),
        ),
        
    )



    for i in range(0, 101):

        pb.value = i * 0.01
        sleep(0.1)
        
        page.update()

            


ft.app(main)