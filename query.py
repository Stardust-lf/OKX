from base_cls.base_operator import BaseOperator

class WalletQuery(BaseOperator):
    def __init__(self):
        super().__init__(name='Query_wallet',url='/api/v5/account/balance')
    def fetch_response(self):
        full_data = self.request_gen.get_response(self.url)
        assert len(full_data['data']) == 1
        wallet_data = full_data['data'][0]['details']
        coin_res = {item['ccy']: item['availBal'] for item in wallet_data}
        return coin_res

class CoinQuery(BaseOperator):
    def __init__(self,ccy:str):
        super().__init__(name='Query_coin_wallet',url='/api/v5/account/balance?ccy={}'.format(str(ccy)))
    def fetch_response(self):
        full_data = self.request_gen.get_response(self.url)
        assert len(full_data['data']) == 1
        coin_data = full_data['data'][0]['details']
        coin_res = {item['ccy']: item['availBal'] for item in coin_data}
        return coin_res


class PriceQuery(BaseOperator):
    def __init__(self,swap_coin:str,base_coin:str):
        super().__init__(name='Query_coin_wallet',url='/api/v5/public/price-limit')
        self.req_body = {'instId':'{}-{}-SWAP'.format(str(swap_coin),str(base_coin))}
    def fetch_response(self):
        #assert len(full_data['data']) == 1
        spot_data = self.request_gen.get_response(self.url,body=self.req_body)['data'][0]
        return {'BuyPriceLimit':spot_data['buyLmt'], 'SellPriceLimit':spot_data['sellLmt'] }



if __name__ == '__main__':
    wq = WalletQuery()
    print(wq.fetch_response())
    cq = CoinQuery(ccy='BTC,ETH')
    print(cq.fetch_response())
    pq = PriceQuery('BTC','USDT')
    print(pq.fetch_response())




