from apistar import Response, http
from apistar.backends.sqlalchemy_backend import Session

from cookies.views import create_fortune


def load_fortunes(session: Session, file: str):
    """
    Utility to load fortunes from a file.
    """
    
    with open(file) as f:
        for line in f:
            create_fortune(session=session, message=line)
            print(f'Loaded fortune: {line}', end='')
