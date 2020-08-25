from cryptopotato import Cryptopotato

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-age': '3600'
}

headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

urls = ["https://cryptopotato.com/opinion-fed-president-calls-on-banks-to-cancel-dividends-is-it-time-for-cryptocurrencies/",
        "https://cryptopotato.com/bitmex-donates-2-5-million-to-bill-gates-foundation-and-others-to-help-against-covid-19/",
        "https://cryptopotato.com/ethereum-price-analysis-200-will-have-to-wait-as-eth-dropped-from-an-important-resistance/",
        "https://cryptopotato.com/financial-crisis-fears-russians-withdrew-more-cash-in-march-2020-than-the-entire-2019-over-trillion-rubles/",
        "https://cryptopotato.com/zcash-price-analysis-zec-surges-35-in-a-week-reaches-new-monthly-high/"]

def test():
    for url in urls:
        Test = Cryptopotato(url, headers)
        Test.populate()
        print(Test.dump())

test()