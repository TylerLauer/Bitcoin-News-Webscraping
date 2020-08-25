from dailyhodl import Dailyhodl

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-age': '3600'
}

headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

urls = ["https://dailyhodl.com/2020/04/20/santander-launches-new-international-money-transfer-service-ripple-and-xrp-technology-not-included/?utm_source=rss&utm_medium=rss&utm_campaign=santander-launches-new-international-money-transfer-service-ripple-and-xrp-technology-not-included",
        "https://dailyhodl.com/2020/04/20/first-regulated-bitcoin-fund-for-institutional-investors-in-hong-kong-gains-approval-from-securities-and-futures-commission/?utm_source=rss&utm_medium=rss&utm_campaign=first-regulated-bitcoin-fund-for-institutional-investors-in-hong-kong-gains-approval-from-securities-and-futures-commission",
        "https://dailyhodl.com/2020/04/20/reddit-crypto-community-reaches-milestone-with-1-million-subscribers/?utm_source=rss&utm_medium=rss&utm_campaign=reddit-crypto-community-reaches-milestone-with-1-million-subscribers",
        "https://dailyhodl.com/2020/04/20/tradingviews-bitcoin-btc-and-xrp-signals-flashing-sell-as-crypto-analysts-warn-market-losing-momentum/?utm_source=rss&utm_medium=rss&utm_campaign=tradingviews-bitcoin-btc-and-xrp-signals-flashing-sell-as-crypto-analysts-warn-market-losing-momentum",
        "https://dailyhodl.com/2020/04/19/facebooks-libra-shifts-to-stablecoins-after-months-of-regulatory-scrutiny-and-fear-of-global-impact/?utm_source=rss&utm_medium=rss&utm_campaign=facebooks-libra-shifts-to-stablecoins-after-months-of-regulatory-scrutiny-and-fear-of-global-impact"]

def test():
    for url in urls:
        Test = Dailyhodl(url, headers)
        Test.populate()
        print(Test.dump())

test()