import requests
import os

URL = "https://picsum.photos/200/300"
FILE_NAME = "image.jpg"
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PATH = f"{PROJECT_ROOT}\{FILE_NAME}"


def download_image(url: str, path):
    res = requests.get(url)
    res.raise_for_status()
    open(path, 'wb').write(res.content)


download_image(url=URL, path=PATH)
