from cointelegraph import Cointelegraph
import sys

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-age': '3600'
}

headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

urls = ["https://cointelegraph.com/news/us-sec-allows-10b-hedge-fund-to-offer-access-to-cme-bitcoin-futures",
        "https://cointelegraph.com/news/real-correlation-bitcoin-price-pumps-follow-us-fed-qe-money-printing",
        "https://cointelegraph.com/news/crypto-scams-on-the-rise-and-can-still-affect-bitcoins-price",
        "https://cointelegraph.com/news/crypto-community-is-keeping-itself-entertained-while-on-coronavirus-lockdown?_ga=2.190304620.679698685.1587127839-1213432947.1586832573",
        "https://cointelegraph.com/news/bitcoin-price-is-showing-3-textbook-technical-signs-of-a-severe-correction",
        "https://cointelegraph.com/news/chinas-internet-finance-association-says-blockchain-is-maturing",
        "https://cointelegraph.com/news/30-days-left-bitcoin-rsi-has-never-been-this-oversold-pre-halving"]

def test():
    for url in urls:
        Test = Cointelegraph(url, headers)
        Test.populate()
        print(Test.dump())

def testContent():
    Test = Cointelegraph(urls[0], headers)
    Test.getContent()

def testDate():
    Test = Cointelegraph(urls[0], headers)
    #Date = Test.getDate()
    #out = Date.replace(',', '')
    #out = out.split(' ')
    #Day = int(out[2])
    #for month in Test.Dates:
    #    if out[1].upper() == month:
    #        Month = int(out[1].upper().replace(month, str(Test.Dates[month])))
    #Year = int(out[3])
    #print(Day)
    #print(Month)
    #print(Year)
    Test.populate()
    print(Test.Day)
    print(Test.Month)
    print(Test.Year)



# Run tests
test()