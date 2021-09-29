"""All the functions in customer_menu."""
from MySQL.UI.menu_function import menu
from MySQL.UI.ui_utils import *
from Mock_db.bank_menu import search_for_customer, open_json
import json


def get_account_number(name):
    json_object = open_json()
    for data in json_object['bank']['customers']:
        if data['name'] == name:
            for account in data['accounts']:
                print(account)


def withdraw_money():
    """Take customer id as input and withdraw money from that customers account."""
    print('Enter customer name: ')
    name = f_input()
    print('Enter amount you want to withdraw: ')
    amount = f_input()
    json_object = open_json()

    for data in json_object['bank']['customers']:
        if data['name'] == name:
            for account in data['accounts']:
                get_account_number(name)
                a_num = int(input('Enter account number: '))
                if account['account_number'] == a_num:
                    account['amount'] -= int(amount)
                    a_file = open("db_files/bank.json", "w")
                    json.dump(json_object, a_file, indent=2)
                    a_file.close()
                break


def insert_money():
    """Take customer id as input and insert money to that customers account."""
    print('Enter customer name: ')
    name = f_input()
    print('Enter amount you want to withdraw: ')
    amount = f_input()
    json_object = open_json()

    for data in json_object['bank']['customers']:
        if data['name'] == name:
            for account in data['accounts']:
                get_account_number(name)
                a_num = int(input('Enter account number: '))
                if account['account_number'] == a_num:
                    account['amount'] += int(amount)
                    a_file = open("db_files/bank.json", "w")
                    json.dump(json_object, a_file, indent=2)
                    a_file.close()
                break


def customer_menu():
    """Display all customer menu options."""
    menu({
        "1": {
            "info": "Search for account",
            "func": search_for_customer
        },
        "2": {
            "info": "Withdraw money",
            "func": withdraw_money
        },
        "3": {
            "info": "Insert money",
            "func": insert_money
        },
        "4": {
            "info": "Exit",
            "func": quit
        }
    })


if __name__ == '__main__':
    customer_menu()