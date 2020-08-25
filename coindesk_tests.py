from coindesk import Coindesk

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-age': '3600'
}

headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

urls = ["https://www.coindesk.com/coinbase-taps-ex-barclays-markets-exec-to-head-institutional-coverage",
        "https://www.coindesk.com/blockchain-now-officially-part-of-chinas-technology-strategy",
        "https://www.coindesk.com/facebook-affirms-libra-commitment-with-50-new-job-openings-in-ireland",
        "https://www.coindesk.com/new-layoffs-hit-ethereum-incubator-consensys",
        "https://www.coindesk.com/bitcoin-news-roundup-for-april-20-2020"]

def test():
    for url in urls:
        Test = Coindesk(url, headers)
        Test.populate()
        print(Test.dump())

test()