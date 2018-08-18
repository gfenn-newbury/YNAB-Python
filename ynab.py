import requests
import os
import json
import time

class YnabAPI:
    def __init__(self):
        self.account = ""
        self.apiKey = ""

    def get_budgets(self):
        try:
            file = open("budget.json",'r')
            self.budgets = json.load(open("budget.json"))
            file.close()
        except IOError:
            key = input("Please enter your API Key:")
            ynab.set_key(key)
            headers = {'Authorization': 'Bearer {}'.format(self.apiKey)}
            response = requests.get('https://api.youneedabudget.com/v1/budgets', headers=headers)
            self.budgets = json.loads(response.text)["data"]["budgets"]
            self.save_to_file(self.budgets, "budget.json")

    def set_key(self, key):
        self.apiKey = key

    def save_to_file(self, data, filename):
        file = open(filename, 'w')
        file.write(json.dumps(data))
        file.close()

    def print_budgets(self):
        print("{:<40} {:<1} {:<11} {:<2} {:<10}".format("Budget Name", "|", "First Month", "|", "Last Month"))
        print("-----------------------------------------------------------------------")
        for budget in self.budgets:
            print("{:<40} {:<1} {:<11} {:<2} {:<10}".format(budget["name"], "|", budget["first_month"], "|",
                                                            budget["last_month"]))
