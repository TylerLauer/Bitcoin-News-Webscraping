from decrypt import Decrypt

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-age': '3600'
}

headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

urls = ["https://decrypt.co/26056/bitcoin-weekly-gains-stock-market",
        "https://decrypt.co/26173/crypto-stocks-take-beating-oil-prices-zero",
        "https://decrypt.co/resources/defi-decentralized-finance-explained-guide-learn",
        "https://decrypt.co/25986/blockchain-app-helps-governments-enforce-coronavirus-quarantines",
        "https://decrypt.co/26042/bitcoin-cryptocurrrency-reddit-subreddit-million"]

def test():
    for url in urls:
        Test = Decrypt(url, headers)
        Test.populate()
        print(Test.dump())

test()