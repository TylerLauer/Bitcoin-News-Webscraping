import requests
from bs4 import BeautifulSoup
import re

class Beincrypto:

    def __init__(self, url, headers):
        self.source_url = "beincrypto.com"
        self.source = "Be[IN]crypto"
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
        self.Author = self.soup.find(class_="jeg_meta_author").text.strip("\n")

    def getTitle(self):
        self.Title = self.soup.find(class_="bc_post_title").text

    def getDate(self):
        Date = self.soup.find(class_="jeg_meta_date").text
        Date = Date.upper()

        #get beginning of date
        for date in self.Dates:
            if Date.find(date) != -1:
                first = Date.index(date)

        #find the end of date string
        end = re.search('[0-9][0-9][0-9][0-9]', Date).end()

        Date = Date[first:end]
        Date = Date.replace(',', '')
        Date = Date.split(' ')

        self.Day = int(Date[1])

        for date in self.Dates:
            if Date[0] == date:
                self.Month = int(self.Dates[date])

        self.Year = int(Date[2])

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