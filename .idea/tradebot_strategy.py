import requests
import time
import hmac
import base64
import hashlib
import json

class TradingBot:
    def __init__(self, base_url, api_key, api_secret, passphrase):
        self.base_url = base_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.passphrase = passphrase

    def _sign(self, timestamp, method, request_path, body=''):
        message = f'{timestamp}{method}{request_path}{body}'
        hmac_key = base64.b64decode(self.api_secret)
        signature = hmac.new(hmac_key, message.encode(), hashlib.sha256).digest()
        return base64.b64encode(signature).decode()

    def _get_timestamp(self):
        return str(time.time())

    def send_request(self, method, request_path, params={}):
        url = self.base_url + request_path
        timestamp = self._get_timestamp()
        headers = {
            'Content-Type': 'application/json',
            'OK-ACCESS-KEY': self.api_key,
            'OK-ACCESS-SIGN': self._sign(timestamp, method, request_path, json.dumps(params) if method == 'POST' else ''),
            'OK-ACCESS-TIMESTAMP': timestamp,
            'OK-ACCESS-PASSPHRASE': self.passphrase,
        }
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers, params=params)
        else:  # POST
            response = requests.post(url, headers=headers, json=params)
        return response.json()

    def place_order(self, symbol, side, size, price=None, order_type='limit'):
        request_path = '/api/v5/trade/order'
        params = {
            'instId': symbol,
            'tdMode': 'cash',
            'side': side,
            'ordType': order_type,
            'sz': size,
        }
        if price:
            params['px'] = price
        return self.send_request('POST', request_path, params)
    def get_historical_prices(self, symbol, interval='1d', limit=100):
        # 这个方法应根据你的交易所API进行实现，下面是一个假设的实现框架
        request_path = f'/api/v5/market/history-candles?instId={symbol}&bar={interval}&limit={limit}'
        response = self.send_request('GET', request_path)
        # 假设响应数据中有历史价格数据，提取并返回
        prices = [float(item[4]) for item in response['data']]  # 假设第5个元素是收盘价
        return prices

class MyStrategy:
    def __init__(self, trading_bot, symbol):
        self.trading_bot = trading_bot
        self.symbol = symbol
        self.short_window = 10
        self.long_window = 50
        # 初始化移动平均线值
        self.short_ma = None
        self.long_ma = None

    def update_moving_averages(self):
        # 获取历史价格数据
        prices = self.trading_bot.get_historical_prices(self.symbol, '1d', max(self.short_window, self.long_window))
        # 计算短期和长期移动平均线
        self.short_ma = np.mean(prices[-self.short_window:])
        self.long_ma = np.mean(prices[-self.long_window:])
        print(f"Updated MA: Short MA={self.short_ma}, Long MA={self.long_ma}")

bot = TradingBot(base_url, api_key, api_secret, passphrase)  # 需要提供实际参数
symbol = 'BTC-USDT'
strategy = MyStrategy(bot, symbol)

strategy.update_moving_averages()
decision = strategy.evaluate_market()
print(f"Market decision: {decision}")

# 根据决策执行策略
strategy.execute_strategy()

