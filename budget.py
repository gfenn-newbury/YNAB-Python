import accounts

from collections import OrderedDict

class budget:
    def __init__(self):
        self.budgetName = ''
        self.accounts = []
    
    def set_budget_name(self, name):
        self.budgetName = name

    def add_account(self, account):
        self.accounts.append(account)

    def make_dict(self):
        accounts = OrderedDict()
        for a in self.accounts:
            accounts[a.accountName] = a.account
        
        budget = OrderedDict()
        budget['name'] = self.budgetName
        budget['accounts'] = accounts
        
        return budget 
