from apistar import Command

from utils import load_fortunes


commands = [
    Command('load_fortunes', load_fortunes),
]
