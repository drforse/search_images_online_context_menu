import webbrowser

import requests
import json

from .base import BaseSearch
from ..exceptions import *


class YandexSearch(BaseSearch):
    base_url: str = 'https://yandex.ru/images/search'
    params: dict = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}

    def get_url(self, image_path: str):
        files = {'upfile': ('blob', open(image_path, 'rb'), 'image/jpeg')}
        r = requests.post(self.base_url, params=self.params, files=files)
        self.check_result(r)
        query_string = json.loads(r.content)['blocks'][0]['params']['url']
        return self.base_url + '?' + query_string

    def search(self, image_path: str):
        try:
            webbrowser.open(self.get_url(image_path))
        except PayloadTooLarge as e:
            self.error = e
            self.error_text = "Яндекс: пук-среньк, файл слишком большой"
        except Exception as e:
            self.error = e
            self.error_text = str(e)
