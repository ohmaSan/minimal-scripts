# Web site word crawler

import requests
from bs4 import BeautifulSoup

target = input("Target: ")


def crawler():
    respons = requests.get(target)
    dirty = BeautifulSoup(respons.content, "lxml")
    clean_list = set(dirty.text.split())
    for clean in clean_list:
        print(clean)


crawler()
