from controllers.app_table import create_table
from controllers.app_context import app_context
from components.banners import table_error_banner
from components.app.table_component import table_component

def app_load(page):

    table = create_table.create_table()

    if table:

        app_context.users = table
    
    else:

        app_context.users = table_error_banner.table_error_table()


    page.go("/app")


def update_table(e):

    table = create_table.create_table()
    app_context.users = table