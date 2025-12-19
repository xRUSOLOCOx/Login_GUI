import flet as ft
from controllers.app_context import app_context
from controllers.router import router

from time import sleep


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
        
        page.on_route_change = lambda route:router.route_change(route,page)
        page.go("/loading")

        sleep(1)
        page.go("/")
        
ft.app(App.page)