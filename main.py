import argparse

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
        print(f"Search engine {search_engine} not supported.")
        input("Press Enter to exit")
        exit()
    search.search(image_path)
    if search.error:
        input("Press Enter to exit")


if __name__ == "__main__":
    main()
