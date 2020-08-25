from beincrypto import Beincrypto

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-age': '3600'
}

headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

urls = ["https://beincrypto.com/covid-19-stimulus-payments-proposed-by-us-representatives/",
        "https://beincrypto.com/cares-act-draws-criticism-over-ivy-league-university-bailouts/",
        "https://beincrypto.com/huobi-treasury-mints-4-2m-husd-in-honor-of-4-20/",
        "https://beincrypto.com/cryptocurrency-news-roundup-for-april-19-2020/",
        "https://beincrypto.com/bbb-researchers-warn-facebook-senior-photo-challenge/"]


def test():
    for url in urls:
        Test = Beincrypto(url, headers)
        Test.populate()
        print(Test.dump())


test()