"""
A simple bank account in 'Happy Bank'.
"""


class BankAccount():
	def __init__(self, name, currency, number, sortcode):
		self.account_balance = 0.0
		self.account_currency = currency
		self.account_number = number
		self.account_sortcode = sortcode
		self.account_name = name

	def __str__(self):
		return "name %s, bank account %s, sortcode %s" % (self.account_name, self.account_number, self.account_sortcode)




girl = BankAccount("Eva", "GBP", "12345678", "123456")
boy = BankAccount("Adam", "GBP", "87654321", "654321")

print girl
print boy

print girl.account_currency
print girl.account_name
print boy.account_number
print boy.account_name
