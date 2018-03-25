from apistar import Include
from apistar.backends import sqlalchemy_backend
from apistar.frameworks.wsgi import WSGIApp

from apistar_cors import CORSMixin
from sqlalchemy import Column, Integer, String

from cookies.models import Base

from commands import commands as custom_commands
from urls import routes as app_routes


class App(CORSMixin, WSGIApp):
    pass


ROUTES = app_routes

SETTINGS = {
    'DATABASE': {
        'URL': 'sqlite:///db.sqlite3',  # TODO: use env variable
        'METADATA': Base.metadata
    }
}

COMMANDS = sqlalchemy_backend.commands + custom_commands

COMPONENTS = sqlalchemy_backend.components

app = App(
    routes=ROUTES,
    settings=SETTINGS,
    commands=COMMANDS,
    components=COMPONENTS
)

if __name__ == '__main__':
    app.main()
