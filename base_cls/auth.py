import base64
import hmac
import requests
import base_cls.utils as utils

BASE_URL = 'https://www.okx.com'

class Signature:
    def __init__(self,auth_param:dict,method:str,url:str,body:dict={}):
        self.auth_param = auth_param
        self.method = method
        self.url = url
        self.body = body
        self.secret = auth_param['APISECRET']
    def get_signature(self, time_str):
        message = time_str + str.upper(self.method) + self.url + str(self.body)
        mac = hmac.new(bytes(self.secret, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
        return base64.b64encode(mac.digest())

class RequestGenerator:
    def __init__(self,auth_param:dict):
        self.auth_param = auth_param

    def get_header(self,time_str,url,method,body):
        signature = Signature(self.auth_param, method=method, url=url, body=body)
        header = dict()
        header['CONTENT-TYPE'] = 'application/json'
        header['OK-ACCESS-KEY'] = self.auth_param['APIKEY']
        header['OK-ACCESS-SIGN'] = signature.get_signature(time_str)
        header['OK-ACCESS-TIMESTAMP'] = time_str
        header['OK-ACCESS-PASSPHRASE'] = self.auth_param['PASS']
        return header

    def get_response(self,url,body:dict={},method:str='GET'):
        if str(body) == '{}' or str(body) == 'None':
            body = ''
        header = self.get_header(str(utils.get_time()), url, method, body)
        url_req = BASE_URL + url
        response = requests.get(url_req, headers=header,params=body)
        response.json()
        return response.json()



