import os
import yaml

class account:

    def __init__(name):
        self.transactions = []
        self.accountName = name
    
    def make_dict(self):
        trans = OrderedDict()

        for t in transactions:
            trans[t.transactionName] = a.make_dict()

        return trans
