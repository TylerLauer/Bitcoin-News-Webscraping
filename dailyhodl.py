import requests
from bs4 import BeautifulSoup
import re

class Dailyhodl:

    def __init__(self, url, headers):
        self.source = "The Daily Hodl"
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
            'JANUARY' : 1,
            'FEBRUARY' : 2,
            'MARCH' : 3,
            'APRIL' : 4,
            'MAY' : 5,
            'JUNE' : 6,
            'JULY' : 7,
            'AUGUST' : 8,
            'SEPTEMBER' : 9,
            'OCTOBER' : 10,
            'NOVEMBER' : 11,
            'DECEMBER' : 12
        }

    def getAuthor(self):
        self.Author = self.soup.find(class_="jeg_meta_author").find('a').text

    def getTitle(self):
        self.Title = self.soup.find(class_="jeg_post_title").text

    def getDate(self):
        Date = self.soup.find(class_='jeg_meta_date').text
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

        #print(Date)

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