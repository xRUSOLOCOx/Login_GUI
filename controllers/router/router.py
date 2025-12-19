from controllers.app_context import app_context
from components.app.main_app_component import main_app_component
from components.main_component import main_component
from components.loading_components.login_loading import login_loading

# Controlador de cambio de vistas:

def route_change(e,page):
        
    app_context.page = page
    page.views.clear()

    if e.route == "/":
        login_view = main_component.main_component()
        page.views.append(login_view)

    elif e.route == "/loading":
        loading_view = login_loading.loading_bar()
        page.views.append(loading_view)

    elif e.route == "/app":
        app_view = main_app_component.main_component()
        page.views.append(app_view)

    page.update()
