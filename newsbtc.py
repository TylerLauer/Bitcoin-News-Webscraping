import requests
from bs4 import BeautifulSoup
import re
import datetime

class Newsbtc:

    def __init__(self, url, headers):
        self.source = "NewsBTC"
        self.url = url
        self.headers = headers
        self.raw = requests.get(self.url, headers=self.headers).content
        self.soup = BeautifulSoup(self.raw, 'html.parser')
        self.Author = None
        self.Title = None
        self.Content = None
        self.Day = None
        self.Month = None
        self.Year = None
        self.Dates = {
            'JAN' : 1,
            'FEB' : 2,
            'MAR' : 3,
            'APR' : 4,
            'MAY' : 5,
            'JUN' : 6,
            'JUL' : 7,
            'AUG' : 8,
            'SEP' : 9,
            'OCT' : 10,
            'NOV' : 11,
            'DEC' : 12
        }

    def getAuthor(self):
        self.Author = self.soup.find(class_="author").text

    def getTitle(self):
        self.Title = self.soup.find(class_="title large").text

    def getDate(self):
        Date = self.url.split('/')
        self.Day = int(Date[5])
        self.Month = int(Date[4])
        self.Year = int(Date[3])

    def getContent(self):
        pass

    def populate(self):
        self.getAuthor()
        self.getTitle()
        self.getDate()

    def toString(self):
        li = "<li>{}<a href='{}'>({})</a>[{}]</li>"
        return li.format(self.Title, self.url, self.source, self.Author)

    def dump(self):
        output = "Title: {} | Url: {} | Source: {} | Author: {} | Day: {} | Month: {} | Year: {}"
        return output.format(self.Title, self.url, self.source, self.Author, self.Day, self.Month, self.Year)