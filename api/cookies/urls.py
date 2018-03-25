from apistar import Route
from apistar.handlers import docs_urls, static_urls

from .views import (
    create_fortune,
    get_fortune,
    get_random_fortune,
    list_fortunes,
    update_fortune,
)

fortune_routes = [
    Route('/', 'GET', get_random_fortune),
    Route('/{uuid}/', 'GET', get_fortune),
    Route('/{uuid}/', 'PATCH', update_fortune),
    Route('/new', 'POST', create_fortune),
    Route('/all', 'GET', list_fortunes),
]
