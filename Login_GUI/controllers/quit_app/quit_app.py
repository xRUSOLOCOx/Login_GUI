from components.quit_app_window import quit_app_window


def quit_app(e,page):

    page.open(quit_app_window.quit_app_window(page))