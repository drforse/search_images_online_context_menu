import argparse
import ctypes
import winsound

from search_images_online.utils import get_search_object_by_engine
from search_images_online.exceptions import SearchEngineNotFound


def main():
    parser = argparse.ArgumentParser(description='search image.')
    parser.add_argument("search_engine", type=str)
    parser.add_argument("image_path", type=str)
    args = parser.parse_args()
    image_path = args.image_path
    search_engine = args.search_engine
    try:
        search = get_search_object_by_engine(search_engine)
    except SearchEngineNotFound:
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        ctypes.windll.user32.MessageBoxW(
            0, f"Search engine {search_engine} not supported.", u"Reverse Image Search Error", 0x1000)
        exit()
    search.search(image_path)
    if search.error:
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        ctypes.windll.user32.MessageBoxW(0, search.error_text, u"Reverse Image Search Error", 0x1000)


if __name__ == "__main__":
    main()
