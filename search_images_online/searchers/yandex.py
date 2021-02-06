import webbrowser
import json
import sqlite3

import requests

from .base import BaseSearch
from ..exceptions import *


class YandexSearch(BaseSearch):
    base_url: str = 'https://yandex.ru/images/search'
    params: dict = {'rpt': 'imageview',
                    'format': 'json',
                    'request': '{"blocks":[{"block":"cbir-controller__upload:ajax"}]}'}

    def get_url(self, image_path: str):
        files = {'upfile': ('blob', open(image_path, 'rb'), 'image/jpeg')}
        r = requests.post(self.base_url, params=self.params, files=files, headers=self.get_headers())
        self.check_result(r)
        query_string = json.loads(r.content)['blocks'][0]['params']['url']
        return self.base_url + '?' + query_string

    def get_headers(self):
        if self._user_agent and self._cookies_file_path.exists() and self._cookies_file_path.is_file():
            return {"User-Agent": self._user_agent, "Cookie": self.get_cookies().encode("utf-8")}
        print("No headers")

    def get_cookies(self) -> str:
        conn = sqlite3.connect(self._cookies_file_path)
        cursor = conn.cursor()
        cursor.execute('SELECT name, value FROM moz_cookies WHERE host IN (".ya.ru", ".yandex.ru")')
        cookies = cursor.fetchall()
        conn.close()
        result = "; ".join([f"{cookie[0]}={cookie[1]}" for cookie in cookies])
        return result

    def search(self, image_path: str):
        try:
            webbrowser.open(self.get_url(image_path))
        except PayloadTooLarge as e:
            self.error = e
            self.error_text = "Яндекс: пук-среньк, файл слишком большой"
        except Exception as e:
            self.error = e
            self.error_text = str(e)
