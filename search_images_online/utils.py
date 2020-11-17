from .searchers.google import GoogleSearch
from .searchers.yandex import YandexSearch
from .exceptions import SearchEngineNotFound
from .searchers.base import BaseSearch


def get_search_object_by_engine(engine) -> BaseSearch:
    if engine == "yandex":
        return YandexSearch()
    if engine == "google":
        return GoogleSearch()
    raise SearchEngineNotFound(engine)
