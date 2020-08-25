from utoday import Utoday

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-age': '3600'
}

headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

urls = ["https://u.today/bitcoin-btc-price-may-skyrocket-right-after-halving-investor-foresees-no-selling-pressure",
        "https://u.today/it-takes-covid-19-or-bitcoin-btc-to-make-banks-better-tyler-winklevoss",
        "https://u.today/bitcoin-btc-now-buys-68880-barrels-of-oil-which-is-more-volatile-cz-binance",
        "https://u.today/bitcoin-btc-is-insurance-during-covid-19-crisis-not-investment-rich-dad-poor-dad-author",
        "https://u.today/heres-why-bitcoin-btc-price-prediction-models-may-now-fail"]

def test():
    for url in urls:
        Test = Utoday(url, headers)
        Test.populate()
        print(Test.dump())

test()