from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    pass


@main.app_errorhandler(500)
def internal_server_error(e):
    pass
