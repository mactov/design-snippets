from configuration import Configuration
from referential import Referential
from authentication import Authentication

class Sandbox(object):
    def __init__(self, account_id = None):
        self.config = Configuration()
        self.budget = None
        self.referential = Referential()
        auth = Authentication
        self.sbx_credentials = 
        if not account_id:
            self.account_id = self.get_available_id()
        else:
            self.account_id = account_id

    def set_budget(self, amount, recipient):
        if not self.budget:
            self.budget = Budget(amount, recipient)
        else:
            self.budget.amount = amount
            self.budget.recipient = recipient
        self.budget.deploy()

    def get_budget(self):
        return self.budget

    def get_available_id(self):
        return self.referential.get_available_id()


if __name__ == '__main__':
    sbx = Sandbox()
    print(sbx.config.get_value('iam'))