from configuration import Configuration


class Budget(object):
	def __init__(self, amount, recipient):
		self.amount = amount
		self.recipient = recipient
		self.config = Configuration()
		self.cuurency = self.config.get_value('currency')