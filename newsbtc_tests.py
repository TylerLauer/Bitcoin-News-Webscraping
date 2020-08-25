from newsbtc import Newsbtc

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-age': '3600'
}

headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

urls = ["https://www.newsbtc.com/2020/04/19/ethereum-to-soon-see-epic-rally-as-buyers-shatter-key-resistance/?utm_source=rss&utm_medium=rss&utm_campaign=ethereum-to-soon-see-epic-rally-as-buyers-shatter-key-resistance",
        "https://www.newsbtc.com/2020/04/20/this-is-bitcoins-fifth-green-week-in-a-row-analysts-think-its-unlikely-the-last/?utm_source=rss&utm_medium=rss&utm_campaign=this-is-bitcoins-fifth-green-week-in-a-row-analysts-think-its-unlikely-the-last",
        "https://www.newsbtc.com/2020/04/20/bitcoin-price-dives-to-6800-leaving-40-million-in-longs-liquidated/?utm_source=rss&utm_medium=rss&utm_campaign=bitcoin-price-dives-to-6800-leaving-40-million-in-longs-liquidated",
        "https://www.newsbtc.com/2020/04/20/what-ive-learned-learned-from-trading-bitcoin-stocks-and-gold-side-by-side/?utm_source=rss&utm_medium=rss&utm_campaign=what-ive-learned-learned-from-trading-bitcoin-stocks-and-gold-side-by-side",
        "https://www.newsbtc.com/2020/04/20/no-americans-are-not-buying-crypto-with-stimulus-checks/?utm_source=rss&utm_medium=rss&utm_campaign=no-americans-are-not-buying-crypto-with-stimulus-checks"]

def test():
    for url in urls:
        Test = Newsbtc(url, headers)
        Test.populate()
        print(Test.dump())

test()