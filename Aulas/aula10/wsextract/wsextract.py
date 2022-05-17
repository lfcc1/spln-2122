"""
Web scraping of links, images and tables.

SYNOPSIS

import ws
...
x = ws_links(url)
y = ws_tables(url)
"""
__version__ = "0.0.2"

from bs4 import BeautifulSoup as BS
from sys import argv
import requests
import json

def ws_links(url):
    """
    ws_links(url): ...
    """
    response = requests.get(url)
    content = response.text
    dt = BS(content, "lxml")
    links = list()
    for link in dt.find_all('a', href=True):
        links.append({"url": link['href'], "text": link.text})
    return links

def main_links():
    for elem in argv[1:]:
        links = ws_links(elem)
        print(json.dumps(links, indent=4, ensure_ascii=False))

def ws_tables(url):
    response = requests.get(url)
    content = response.text
    dt = BS(content, "lxml")
    tables = list()
    for table in dt.find_all('table'):
        t = list()
        for tr in table.find_all('tr'):
            row = list()
            for td in tr.find_all(['td','th']):
               row.append(td.text)
            t.append(row)
        tables.append(t)

    return tables

def main_tables():
    for elem in argv[1:]:
        tables = ws_tables(elem)
        print(json.dumps(tables, indent=4, ensure_ascii=False))


