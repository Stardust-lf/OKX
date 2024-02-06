from query import WalletQuery,CoinQuery,PriceQuery

wq = WalletQuery()
print(wq.fetch_response())
cq = CoinQuery(ccy='BTC,ETH')
print(cq.fetch_response())
pq = PriceQuery('BTC','USDT')
print(pq.fetch_response())
