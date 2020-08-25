from cryptoglobe import Cryptoglobe

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-age': '3600'
}

headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

urls = ["https://www.cryptoglobe.com/latest/2020/04/crypto-hedge-fund-ceo-predicts-supply-shock-following-bitcoins-halving/",
        "https://www.cryptoglobe.com/latest/2020/04/google-chrome-removes-49-malicious-extensions-targeting-cryptocurrency-wallets/",
        "https://www.cryptoglobe.com/latest/2020/04/one-of-the-worlds-largest-hedge-funds-is-now-trading-bitcoin-futures/",
        "https://www.cryptoglobe.com/latest/2020/04/goldman-sachs-us-companies-will-reduce-cash-spending-by-a-record-33/",
        "https://www.cryptoglobe.com/latest/2020/04/kansas-city-fed-on-correlation-of-bitcoin-with-the-s-p-500/"]

def test():
    for url in urls:
        Test = Cryptoglobe(url, headers)
        Test.populate()
        print(Test.dump())

test()