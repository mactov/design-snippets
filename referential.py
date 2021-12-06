from os import path
import json


class Referential(object):
    def __init__(self, credentials):
        self.__dict = None
        if path.exists('referential.json'):
            with open('referential.json', 'r') as f:
                self.__dict = json.load(f)

    def get_available_id(self):
        pass

    def read_account_info(self, account_id):
        pass

    def update_account_info(self, account_id, payload):
        pass