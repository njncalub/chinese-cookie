from apistar import Command
from apistar.backends import sqlalchemy_backend

from main.utils import load_fortunes


commands = sqlalchemy_backend.commands + [
    Command('load_fortunes', load_fortunes),
]
