import webbrowser

from ..exceptions import *


class BaseSearch:
    base_url: str = ''
    params: dict = {}

    def __init__(self):
        self.error = None
        self.error_text: str = ""

    def get_url(self, image_path: str) -> str:
        raise NotImplementedError

    def search(self, image_path: str):
        try:
            webbrowser.open(self.get_url(image_path))
        except PayloadTooLarge as e:
            self.error = e
            self.error_text = "Файл слишком большой"
        except Exception as e:
            self.error = e
            self.error_text = str(e)

    def check_result(self, result):
        if result.status_code == 200:
            return
        if result.status_code == 413:
            raise PayloadTooLarge
        raise Exception(f"Unexpected error: {result.status_code}")
