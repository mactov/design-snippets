from configuration import Configuration
from cloudformation import CloudFormation


class Budget(object):
	def __init__(self, amount, credentials, recipient):
		self.config = Configuration()
		self.amount = amount
		self.recipient = recipient
		self.config = Configuration()
		self.currency = self.config.get_value('currency')
		self.cfn = CloudFormation(credentials=credentials, region=self.config.get_value('region'))

	def deploy_stack(self, self.stack_name(), self.stack_template(), self.stack_parameters()):
		pass

	def stack_name(self):
		pass

	def stack_template(self):
		pass

	def stack_parameters(self):
		pass