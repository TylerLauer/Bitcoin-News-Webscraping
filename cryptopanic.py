import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

class Cryptopanic:

    def __init__(self, headers):
        self.url = "http://www.cryptopanic.com"
        self.headers = headers
        self.raw = requests.get(self.url, headers=headers).content
        self.soup = BeautifulSoup(self.raw, 'html.parser')
        self.urls = []


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-age': '3600'
}

headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})


test = Cryptopanic(headers)
print(test.soup.find(class_="news-container ps"))