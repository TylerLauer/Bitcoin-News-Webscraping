import requests
from bs4 import BeautifulSoup

def getSoup(self, url, headers):
    raw_html = requests.get(url, headers=headers).content
    return BeautifulSoup(raw_html, 'html.parser')