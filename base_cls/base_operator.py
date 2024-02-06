from base_cls.auth import RequestGenerator
import base_cls.utils as utils
import json
# auth_param = configReader.get_auth()
# request_gen = RequestGenerator(auth_param)
# print(request_gen.get_response('/api/v5/account/balance'))

class BaseOperator:
    def __init__(self,name:str='Base',url:str='',body:dict={}):
        self.operation_name = name
        self.request_gen = RequestGenerator(utils.get_auth_config())
        self.url = url
        self.body = body

    def fetch_response(self):
        return
    def get_operation_name(self):
        return self.operation_name
    def store_history(self):
        return
    def get_url(self):
        return self.url
    def get_request_gen(self):
        return self.request_gen

class BaseListenerConfig:
    def __init__(self,name:str='BaseListener'):
        self.listener_name = name
    def get_listener_name(self):
        return self.listener_name

    def on_open(self,ws):
        return
    def on_message(self, ws, message):
        return
    def on_error(self, ws, error):
        return
    def on_close(self, ws):
        return