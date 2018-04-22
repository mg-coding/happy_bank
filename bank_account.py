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
		self.account_transactions_list = []

	def __str__(self):
		return "name %s, bank account %s, sortcode %s" % (self.account_name, self.account_number, self.account_sortcode)

	def add_transaction(self, transaction):
		self.account_transactions_list.append(transaction) #append(transaction) is adding transactions to the account_transaction_list (so you know what I bought)
		amount = transaction["amount"]
		if transaction["payment type"] == "payment out":
			self.account_balance -= amount
		elif transaction["payment type"] == "payment in":
			self.account_balance += amount






girl = BankAccount("Eva", "GBP", "12345678", "123456")
boy = BankAccount("Adam", "GBP", "87654321", "654321")

print girl
print boy

print girl.account_currency
print girl.account_name
print boy.account_number
print boy.account_name

print girl.account_transactions_list

sample_transaction = {"amount" : 2.50, "currency" : "GBP", "description" : "coffee", "date" : "April 2018", "payment type" : "payment out"}
paymentin_transaction = {"amount" : 5.0, "currency" : "GBP", "description" : "money in", "date" : "April 2018", "payment type" : "payment in"}


print girl.account_balance
girl.add_transaction(sample_transaction)
print girl.account_transactions_list
print girl.account_balance


print boy.account_balance
boy.add_transaction(sample_transaction)
print boy.account_transactions_list
print boy.account_balance


print girl.account_balance
girl.add_transaction(paymentin_transaction)
print girl.account_balance


print boy.account_balance
boy.add_transaction(paymentin_transaction)
print boy.account_balance











