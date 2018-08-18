import requests
import os
import json
import time
import ynab

def menu(ynabClient):
    while True:
        print("\n\n\n0. Exit\n"
            "1. Print Budgets"
            ""
            ""
            ""
            "")
        result = raw_input("Choice: ")
        if result == '0':
            return
        elif result == '1':
            ynabClient.print_budgets()
            time.sleep(10)


def main():
    ynabClient = ynab.YnabAPI()
    try:
        file = open("budget.json", 'r')
        file.close()
        newData = raw_input("Refresh Data? ")
        if newData == 'y':
            os.remove("budget.json")
        ynabClient.get_budgets()
    except IOError:
        ynabClient.get_budgets()
    menu(ynabClient)

if __name__ == '__main__':
    main()
