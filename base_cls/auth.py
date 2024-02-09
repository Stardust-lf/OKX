import base64
import hmac
import requests
import base_cls.utils as utils

BASE_URL = 'https://www.okx.com'

class Signature:
    def __init__(self,secret, request_param:utils.RequestParam):
        self._request_param = request_param.get_params()
        self._secret = secret
    def get_signature(self, time_str):
        message = (time_str + str.upper(self._request_param['METHOD'])
                   + self._request_param['URL']
                   + str(self._request_param['BODY']))
        mac = hmac.new(bytes(self._secret, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
        return base64.b64encode(mac.digest())

class RequestGenerator:
    def __init__(self,signature: Signature, request_param: utils.RequestParam):
        self._request_param = request_param.get_params()
        if str(self._request_param['BODY']) == '{}':
            self._request_param['BODY'] = ''
        self._signature = signature
        self._auth_param = utils.get_auth_config()
    def get_header(self,time_str):
        header = dict()
        header['CONTENT-TYPE'] = 'application/json'
        header['OK-ACCESS-KEY'] = self._auth_param['APIKEY']
        header['OK-ACCESS-SIGN'] = self._signature.get_signature(time_str)
        header['OK-ACCESS-TIMESTAMP'] = time_str
        header['OK-ACCESS-PASSPHRASE'] = self._auth_param['PASS']
        return header

    def get_response(self):
        header = self.get_header(str(utils.get_time()))
        print(header)
        url_req = BASE_URL + self._request_param['URL']
        response = requests.get(url_req, headers=header,params=self._request_param['BODY'])
        response.json()
        return response.json()



