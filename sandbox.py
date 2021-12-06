from configuration import Configuration
from referential import Referential
from authentication import Authentication

class Sandbox(object):
    class SandboxError(Exception):
        pass

    def __init__(self, account_id = None):
        self.config = Configuration()
        self.budget = None
        if not account_id:
            self.account_id = self.get_available_id()
        else:
            if self.is_valid_account_id(account_id):
                self.account_id = account_id
            else:
                raise 
        self.region = self.config.get_value('region')
        self.role = self.config.get_value('role')
        self.cred_file = self.config.get_value('cred_file')
        auth = Authentication()
        self.sbx_credentials = auth.authenticate(self.account_id, self.region, self.role, self.cred_file)
        self.socle_credentials = auth.authenticate(self.account_id, self.region, self.role, self.cred_file)
        self.referential = Referential(self.socle_credentials)
        self.props = self.load_props()

    def set_budget(self, amount, recipient):
        if not self.budget:
            self.budget = Budget(amount, self.sbx_credentials, recipient)
        else:
            self.budget.amount = amount
            self.budget.recipient = recipient
        self.budget.deploy()
        self.referential.update_account_info(self.dump_props())

    def get_budget(self):
        return self.budget

    def get_available_id(self):
        return self.referential.get_available_id()

    def load_props(self)
        pass

    def dump_props(self)
        pass

    def is_valid_account_id(self):
        return True

if __name__ == '__main__':
    sbx = Sandbox()
    print(sbx.config.get_value('iam'))