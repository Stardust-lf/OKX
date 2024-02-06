from base_cls.base_operator import BaseListenerConfig
import websocket
import json

websocket.enableTrace(True)

class PriceLimitListener(BaseListenerConfig):
    def __init__(self):
        super().__init__(name='Price_limit_listener')
    def on_message(self, ws, message):
        print('Message from', self.listener_name)
        print(message)
        return message

    def on_error(self, ws, error):
        print('Error from', self.listener_name)
        print(error)

    def on_close(self, ws):
        print('Connection {} closed'.format(self.get_listener_name()))

    def on_open(self,ws):
        subscribe_message = {
            "op": "subscribe",
            "args": [{
                "channel": "price-limit",
                "instId": "BTC-USD"
            }]
        }
        ws.send(json.dumps(subscribe_message))

    def listen(self):
        ws = websocket.WebSocketApp("wss://ws.okx.com:8443/ws/v5/business",
                              on_error = self.on_error,
                              on_close = self.on_close)
        ws.on_open = self.on_open
        ws.run_forever()

if __name__ == '__main__':
    pll = PriceLimitListener()
    pll.listen()
