# from behave import given, when, then
# from transaction_service.domain.account import Account, Transaction
#
#
# # Mock implementations of TransactionRepository and BalanceUpdates
# class TransactionRepository:
#     def __init__(self):
#         self.transactions = []
#
#     def store(self, transaction):
#         self.transactions.append(transaction)
#
# class BalanceUpdates:
#     def __init__(self):
#         self.updates = []
#
#     def produce(self, balance_update):
#         self.updates.append(balance_update)
#
# # A dictionary to represent a simple database of accounts
# accounts_db = {}
#
# transaction_repository = TransactionRepository()
# balance_updates = BalanceUpdates()
#
# @given('an account {account_id:d} has balance {balance:d}')
# def step_impl(context, account_id, balance):
#     transactions = [Transaction(id=str(i), account_number=str(account_id), amount=balance) for i in range(1)]
#     account = Account(account_id, transaction_repository, balance_updates, transactions)
#     accounts_db[account_id] = account
#
# @given('there is not account with the number {account_id:d}')
# def step_impl(context, account_id):
#     if account_id in accounts_db:
#         del accounts_db[account_id]
#
# @when('an account {account_id:d} is credited with {amount:d}')
# def step_impl(context, account_id, amount):
#     try:
#         account = accounts_db[account_id]
#         account.credit(amount)
#         context.exception = None
#     except KeyError as e:
#         context.exception = e
#         context.account_id = account_id
#
# @when('an account {account_id:d} is debited with {amount:d}')
# def step_impl(context, account_id, amount):
#     try:
#         account = accounts_db[account_id]
#         account.debit(amount)
#         context.exception = None
#     except KeyError as e:
#         context.exception = e
#         context.account_id = account_id
#
# @then('a account {account_id:d} should have a balance of {expected_balance:d}')
# def step_impl(context, account_id, expected_balance):
#     account = accounts_db[account_id]
#     assert account.balance == expected_balance, f"Expected {expected_balance}, but got {account.balance}"
#
# @then('a bad transaction should be reported')
# def step_impl(context):
#     assert isinstance(context.exception, KeyError), "Expected KeyError but got no exception"
#     print(context.exception)
#     print(context.account_id)
#     assert str(context.exception) == str(context.account_id), "Unexpected error message"
