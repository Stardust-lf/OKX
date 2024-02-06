import configparser
import base64
import datetime as dt
import hmac
import requests

class ConfigReader:
    def __init__(self,config_parser:configparser.ConfigParser,file_path:str):
        self.config_parser = config_parser
        self.config_parser.read(file_path)
    # def get_config(self):
    #     return self.config_parser.items()
    def get_auth(self):
        auth_info = dict(self.config_parser.items('AUTH_INFO'))
        return {'APIKEY':auth_info['access-key'],'APISECRET':auth_info['access-secret'],'PASS':auth_info['access-passphrase']}
#
# def send_signed_request(http_method, url_path, payload={}):
#     def get_time():
#         return dt.datetime.utcnow().isoformat()[:-3] + 'Z'
#
#     def signature(timestamp, method, request_path, body, secret_key):
#         if str(body) == '{}' or str(body) == 'None':
#             body = ''
#         message = str(timestamp) + str.upper(method) + request_path + str(body)
#         mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
#         d = mac.digest()
#         return base64.b64encode(d)
#
#     # set request header
#     def get_header(request='GET', endpoint='', body: dict = dict()):
#         cur_time = get_time()
#         header = dict()
#         header['CONTENT-TYPE'] = 'application/json'
#         header['OK-ACCESS-KEY'] = APIKEY
#         header['OK-ACCESS-SIGN'] = signature(cur_time, request, endpoint, body, APISECRET)
#         header['OK-ACCESS-TIMESTAMP'] = str(cur_time)
#         header['OK-ACCESS-PASSPHRASE'] = PASS
#         return header
#
#     url = BASE_URL + url_path
#     header = get_header(http_method, url_path, payload)
#     response = requests.get(url, headers=header)
#     response.json()
#     return response.json()
#
# balance = send_signed_request("GET", "/api/v5/account/balance", payload={})
# for item in balance['data']:
#     wallet = item['details']
#     for coin in wallet:
#         print(coin['availBal'],coin['ccy'])

