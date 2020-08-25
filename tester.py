from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import requests
import pdfkit
import re

#driver = webdriver.Chrome(ChromeDriverManager().install())

#driver.set_page_load_timeout(10)

#driver.get("https://cryptopanic.com/news/news-sites")


#test = driver.find_element_by_class_name("si-source-domain")

#actions = ActionChains(driver)
#actions.move_to_element(test).click().perform()

#print(test)

#pdfkit.from_url('https://cointelegraph.com/news/us-sec-allows-10b-hedge-fund-to-offer-access-to-cme-bitcoin-futures', './test.pdf')

#Dates = {
#            'JAN' : 1,
#            'FEB' : 2,
#            'MAR' : 3,
#            'APR' : 4,
##            'MAY' : 5,
#            'JUN' : 6,
#            'JUL' : 7,
#            'AUG' : 8,
#            'SEP' : 9,
#            'OCT' : 10,
#            'NOV' : 11,
#            'DEC' : 12
#        }

#test = "								Updated								Apr 20, 2020								by								"
#test = test.upper()


#for date in Dates:
#    if test.find(date) != -1:
#        first = test.index(date)
#print(test[23:35])

#end = re.search('[0-9][0-9][0-9][0-9]', test).end()

#test = test[first:end]
#test = test.replace(',', '')
#test = test.split(' ')

#Day = test[1]

#for date in Dates:
#    if test[0] == date:
#        Month = Dates[date]

#Year = test[2]

#print(test)
#print(Day)
#print(Month)
#print(Year)


Dates = {
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



headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-age': '3600'
}

headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

urls = ["https://bitcoinist.com/bitcoin-could-hit-9k-in-q2-as-price-jumps-short-term-moving-average/",
        "https://bitcoinist.com/interview-with-adam-todd-founder-ceo-digitex-futures/",
        "https://bitcoinist.com/chainlink-cryptocurrency-is-up-100-percent-ytd-whats-behind-the-intense-rally/",
        "https://bitcoinist.com/if-you-bought-1000-of-xrp-six-years-ago-it-would-be-worth-67000-now/",
        "https://bitcoinist.com/420-day-in-crypto-remembering-the-class-of-altcoins-that-went-up-in-smoke/"]



raw = requests.get("https://u.today/bitcoin-btc-price-may-skyrocket-right-after-halving-investor-foresees-no-selling-pressure", headers=headers).content

soup = BeautifulSoup(raw, 'html.parser')

Date = soup.find(class_='humble author__item-time').text

print(Date)

Date = Date.split(',')

print(Date)

Date = Date[1]

print(Date)

#find the end of date string
end = re.search('[0-9][0-9][0-9][0-9]', Date).end()

Date = Date[0:end]

print(Date)

Date = Date.replace(' ', '')

Date = Date.split('/')

print(Date)

Day = int(Date[1])
Month = int(Date[0])
Year = int(Date[2])
print(Day)
print(Month)
print(Year)















#print(driver.find_element_by_class_name("news"))
#print(driver.page_source)

#soup = BeautifulSoup(driver.page_source, 'html.parser')

#for link in soup.find_all(class_="news-row news-row-link"):
#    print(link.find('a', href=True)['href'])

def getUrl(soup):
    # get the link from cryptopanic
    link = soup.find('a', href=True)['href']
    link = link.split('/')[3]

    # get the domain from cyptopanic
    domain = soup.find(class_="si-source-domain").text
    domain = "http://www." + domain

    print(domain + '/' + link)



#for div in soup.find_all(class_="news-row news-row-link"):
    #print(news_div.find(class_="si-source-domain").text)
#    getUrl(div)