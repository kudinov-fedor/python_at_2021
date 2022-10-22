import requests
import os

URL = "https://picsum.photos/200/300"
FILE_NAME = "image.jpg"
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PATH = f"{PROJECT_ROOT}\{FILE_NAME}"


def test_download_image():
    res = requests.get(URL)
    res.raise_for_status()
    open(PATH, 'wb').write(res.content)
