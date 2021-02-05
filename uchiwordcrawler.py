# Website word crawler

import requests
from bs4 import BeautifulSoup

target = input("Target: ")
print("#" * 50 + "\n")


def crawler():
    respons = requests.get(target)
    dirty = BeautifulSoup(respons.content, "lxml")
    clean_list = set(dirty.text.split())
    for clean in clean_list:
        print(clean.strip(',').strip('.').strip('"').strip(':').strip('(').strip(')').strip(':'))
    print(f"\nNumber of Words: {len(clean_list)}")


crawler()
