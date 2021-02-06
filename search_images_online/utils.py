from .searchers.google import GoogleSearch
from .searchers.yandex import YandexSearch
from .exceptions import SearchEngineNotFound, ConfigError
from .searchers.base import BaseSearch


def get_search_object_by_engine(engine) -> BaseSearch:
    if engine == "yandex":
        try:
            from config import yandex_cookies_file_path, user_agent
        except ImportError:
            raise ConfigError("yandex_cookies_file_path or user_agent not found in config")
        return YandexSearch(yandex_cookies_file_path, user_agent)
    if engine == "google":
        return GoogleSearch()
    raise SearchEngineNotFound(engine)
