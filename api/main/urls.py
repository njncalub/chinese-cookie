from apistar import Include
from apistar.handlers import docs_urls, static_urls

from fortunes.urls import fortune_routes


routes = [
    Include('/fortunes', fortune_routes),
    
    Include('/docs', docs_urls),
    Include('/static', static_urls),
]
