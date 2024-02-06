import Auth
import configparser

configReader = Auth.ConfigReader(config_parser=configparser.ConfigParser(),file_path='Config.ini')
print(configReader.get_auth())