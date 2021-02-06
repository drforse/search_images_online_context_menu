import json
import webbrowser
from pathlib import Path
from typing import Optional

from ..exceptions import *


class BaseSearch:
    base_url: str = ''
    params: dict = {}

    def __init__(self, cookies_file_path: Optional[Path] = None, user_agent: Optional[str] = None):
        self.error = None
        self.error_text: str = ""
        self._cookies_file_path = cookies_file_path
        self._user_agent = user_agent

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
        if result.status_code == 413:
            raise PayloadTooLarge
        if result.status_code != 200:
            raise Exception(f"Unexpected error: {result.status_code}")
        content = json.loads(result.content)
        if content.get("type") == "captcha":
            raise CaptchaOccurred
