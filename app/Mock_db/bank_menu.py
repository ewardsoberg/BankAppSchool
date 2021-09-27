"""All the functions from bank menu."""
from MySQL.UI.menu_function import menu
from MySQL.UI.ui_utils import *
import json


def open_json():
    with open('db_files/bank.json') as f:
        data = json.load(f)
        return data


def search_for_customer():
    """Take user input first and last name and gets that user."""
    data = open_json()
    print('Enter customer name: ')
    name = f_input()
    for data in data['customers']:
        if data['name'] == name:
            print(data)


def show_all_customers():
    """Show all the customer."""
    data = open_json()
    for data in data['customers']:
        print(data)


def register_new_customer():
    """Take a dict and creates a new customer."""
    insert_dict = {}
    print('Enter name: ')
    name = f_input()
    account = [None]
    insert_dict['name'] = name
    insert_dict['accounts'] = account
    with open('db_files/bank.json', 'r+') as file:
        data = json.load(file)
        data['customers'].append(insert_dict)
        file.seek(0)
        json.dump(data, file)


def add_account_to_customer():
    """Add new bank account to an existing customer."""
    insert_dict = {}
    print('Enter you name: ')
    name = f_input()
    print('Enter currency: ')
    currency = f_input()
    print('Enter amount: ')
    amount = f_input()
    insert_dict['currency'] = currency
    insert_dict['amount'] = amount
    number_list = []
    with open('db_files/bank.json', 'r+') as file:
        data = json.load(file)
        for data in data['customers']:
            for accounts in data['accounts']:
                if accounts:
                    number_list.append(accounts['account_number'])

def bank_menu():
    """Display all bank menu options."""
    menu({
        "1": {
            "info": "Search for customer",
            "func": search_for_customer
        },
        "2": {
            "info": "Show all customers",
            "func": show_all_customers
        },
        "3": {
            "info": "Register new customer",
            "func": register_new_customer
        },
        "4": {
            "info": "Add new account to customer",
            "func": add_account_to_customer
        },
        "5": {
            "info": "Exit",
            "func": quit
        }
    })


if __name__ == '__main__':
    bank_menu()
