from apistar import environment, typesystem

from main.models import Base


class Env(environment.Environment):
    properties = {
        'DEBUG': typesystem.boolean(default=True),
        'DATABASE_URL': typesystem.string(default='sqlite:///db.sqlite3'),
    }


env = Env()

settings = {
    'DATABASE': {
        'URL': env['DATABASE_URL'],
        'METADATA': Base.metadata,
    }
}
