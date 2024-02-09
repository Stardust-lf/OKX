from query import WalletQuery, CoinQuery, PriceQuery
from base_cls.base_operator import BaseOperator


# wq = WalletQuery()
# print(wq.fetch_response())
# cq = CoinQuery(ccy='BTC,ETH')
# print(cq.fetch_response())
# pq = PriceQuery('BTC','USDT')
# print(pq.fetch_response())
def test_operator(operator: BaseOperator):
    print(operator.fetch_response())


if __name__ == '__main__':
    test_operator(WalletQuery())
    test_operator(CoinQuery('BTC,ETH'))
    test_operator(PriceQuery('BTC', 'USDT'))
