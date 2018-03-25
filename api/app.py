from apistar import Include
from apistar.backends import sqlalchemy_backend
from apistar.frameworks.wsgi import WSGIApp as App

from sqlalchemy import Column, Integer, String

from cookies.models import Base

from commands import commands as custom_commands
from urls import routes


settings = {
    'DATABASE': {
        'URL': 'sqlite:///db.sqlite3',
        'METADATA': Base.metadata
    }
}

commands = sqlalchemy_backend.commands + custom_commands

components = sqlalchemy_backend.components

app = App(
    routes=routes,
    settings=settings,
    commands=commands,
    components=components
)

if __name__ == '__main__':
    app.main()
