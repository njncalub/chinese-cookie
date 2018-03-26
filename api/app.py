from apistar import Include
from apistar.backends import sqlalchemy_backend
from apistar.frameworks.wsgi import WSGIApp

from apistar_cors import CORSMixin
from sqlalchemy import Column, Integer, String

from main.commands import commands as COMMANDS
from main.components import components as COMPONENTS
from main.urls import routes as ROUTES
from main.settings import settings as SETTINGS


class App(CORSMixin, WSGIApp):
    pass


app = App(
    commands=COMMANDS,
    components=COMPONENTS,
    routes=ROUTES,
    settings=SETTINGS
)

if __name__ == '__main__':
    app.main()
