from os import path
import json


class Referential(object):
    def __init__(self):
        self.__dict = None
        if path.exists('referential.json'):
            with open('referential.json', 'r') as f:
                self.__dict = json.load(f)

    def get_available_id(self):
        pass