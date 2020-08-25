from btcmanager import Btcmanager

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-age': '3600'
}

headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

urls = ["https://btcmanager.com/hong-kong-sfc-bitcoin-btc-fund-institutional-investors/",
        "https://btcmanager.com/binance-ontology-asset-chain-trading-cryptocurrency/",
        "https://btcmanager.com/kucoin-onchain-custodian-funds-lockton-insurance/",
        "https://btcmanager.com/japanese-content-creators-blockchain-technology-use-case/",
        "https://btcmanager.com/ethereum-2-0-launch-inches-closer-as-genesis-block-gets-mined-on-testnet/"]

def test():
    for url in urls:
        Test = Btcmanager(url, headers)
        Test.populate()
        print(Test.dump())

test()