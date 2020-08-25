from zycrypto import Zycrypto

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-age': '3600'
}

headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

urls = ["https://zycrypto.com/over-1000-per-bitcoin-transaction-roger-ver-tenders-bitcoin-cash-as-a-sharpened-substitute/",
        "https://zycrypto.com/binance-completes-11th-bnb-burn-erasing-more-than-10-of-total-supply/",
        "https://zycrypto.com/bitmex-donates-2-5-million-towards-covid-19-relief-efforts/",
        "https://zycrypto.com/the-uncorrelated-and-idiosyncratic-nature-of-bitcoin/",
        "https://zycrypto.com/ethereum-2-0-game-changer-testnet-nears-20000-validators-within-two-days/"]

def test():
    for url in urls:
        Test = Zycrypto(url, headers)
        Test.populate()
        print(Test.dump())

test()