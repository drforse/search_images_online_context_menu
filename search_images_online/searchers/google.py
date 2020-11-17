import requests

from .base import BaseSearch


class GoogleSearch(BaseSearch):
    base_url: str = 'http://www.google.com/searchbyimage/upload'

    def get_url(self, image_path: str):
        files = {'encoded_image': (image_path, open(image_path, 'rb')), 'image_content': ''}
        r = requests.post(self.base_url, params=self.params, files=files)
        self.check_result(r)
        return r.url.replace("webhp", "search")
