from base_cls.base_operator import BaseOperator
from base_cls.auth import RequestGenerator, Signature
from base_cls.utils import RequestParam, get_secret_config


class WalletQuery(BaseOperator):
    def __init__(self):
        _rpm = RequestParam('/api/v5/account/balance', 'GET', body={})
        _secret = get_secret_config()
        _signature = Signature(_secret, _rpm)
        self._rp = RequestGenerator(_signature, _rpm)
        super().__init__(name='Query_wallet', request=self._rp)

    def fetch_response(self):
        full_data = self._rp.get_response()
        assert len(full_data['data']) == 1
        wallet_data = full_data['data'][0]['details']
        coin_res = {item['ccy']: item['availBal'] for item in wallet_data}
        return coin_res


class CoinQuery(BaseOperator):
    def __init__(self, ccy:str):
        _rpm = RequestParam('/api/v5/account/balance?ccy={}'.format(str(ccy)), 'GET', body={})
        _secret = get_secret_config()
        _signature = Signature(_secret, _rpm)
        self._rp = RequestGenerator(_signature, _rpm)
        super().__init__(name='Query_coin_wallet', request=self._rp)

    def fetch_response(self):
        full_data = self._rp.get_response()
        assert len(full_data['data']) == 1
        coin_data = full_data['data'][0]['details']
        coin_res = {item['ccy']: item['availBal'] for item in coin_data}
        return coin_res


class PriceQuery(BaseOperator):
    def __init__(self, swap_coin: str, base_coin: str):
        _rpm = RequestParam('/api/v5/public/price-limit', 'GET',
                            body={'instId': '{}-{}-SWAP'.format(str(swap_coin), str(base_coin))})
        _secret = get_secret_config()
        _signature = Signature(_secret, _rpm)
        self._rp = RequestGenerator(_signature, _rpm)
        super().__init__(name='Query_coin_wallet', request=self._rp)

    def fetch_response(self):
        # assert len(full_data['data']) == 1
        spot_data = self._rp.get_response()['data'][0]
        return {'BuyPriceLimit': spot_data['buyLmt'], 'SellPriceLimit': spot_data['sellLmt']}


if __name__ == '__main__':
    wq = WalletQuery()
    print(wq.fetch_response())
    cq = CoinQuery(ccy='BTC,ETH')
    print(cq.fetch_response())
    pq = PriceQuery('BTC', 'USDT')
    print(pq.fetch_response())
