from os import getenv, path
import json

class Configuration(object):
    def __init__(self):
        self.__dict = None
        env = getenv('ENV', 'local')
        if path.exists(f'config-{env}.json'):
            with open(f'config-{env}.json', 'r') as f:
                self.__dict = json.load(f)

    def get_value(self, key):
        if key in self.__dict.keys():
            return self.__dict[key]
        return None

    def __str__(self):
        return f'Config: {self.__dict}'

