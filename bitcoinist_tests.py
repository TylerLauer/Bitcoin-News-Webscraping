from bitcoinist import Bitcoinist

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

def test():
    for url in urls:
        Test = Bitcoinist(url, headers)
        Test.populate()
        print(Test.dump())

test()