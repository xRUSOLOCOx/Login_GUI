import flet as ft
from components.main_component import main_component
from controllers.app_context import app_context


class App:

    def page(page:ft.Page):

        app_context.page = page

        page.title = "LOGIN_GUI"
        page.padding = 0


        page.window.width = 1200
        page.window.height = 700

        page.window.min_width = 760
        page.window.min_height = 700
        page.window.max_width = 1200
        page.window.max_height = 700
        
        page.bgcolor = "#1b1d1e"

        page.add(

            main_component.main_component()

        )

ft.app(App.page)