import flet as ft
from components.main_component import main_component

class App:


    def page(page:ft.Page):

        page.title = "LOGIN_GUI"
        page.padding = 0


        page.window.width = 1200

        page.window.min_width = 700
        page.window.min_height = 700
        page.window.max_width = 1200
        page.window.max_height = 700


        page.add(

            main_component.main_component()

        )








ft.app(App.page)