import datetime as dt
import sys
import configparser
import argparse

parser = argparse.ArgumentParser(description='Enter your OKX API payloads')
parser.add_argument('-k',type=str, required=True, help='Enter KEYSECRET')
parser.add_argument('-p',type=str,required=True,help='Enter PASSWORD')
def get_params():
    args = parser.parse_args()
    return [args.k,args.p]

def get_time():
    return dt.datetime.utcnow().isoformat()[:-3] + 'Z'

def get_config_parser():
    return configparser.ConfigParser()

class ConfigReader:
    def __init__(self,passwd:str,secret:str,config_parser:configparser.ConfigParser,file_path:str):
        self.config_parser = config_parser
        self.config_parser.read(file_path)
        self.passwd = passwd
        self.secret = secret
    # def get_config(self):
    #     return self.config_parser.items()
    def get_auth(self):
        auth_info = dict(self.config_parser.items('AUTH_INFO'))
        return {'APIKEY':auth_info['access-key'],'APISECRET':self.secret,'PASS':self.passwd}

def get_auth_config():
    sys_param = get_params()
    configReader = ConfigReader(sys_param[1], sys_param[0], config_parser=get_config_parser(), file_path='base_cls/configs/Config.ini')
    return configReader.get_auth()


