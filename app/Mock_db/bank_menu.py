"""All the functions from bank menu."""
from MySQL.UI.menu_function import menu
from MySQL.UI.ui_utils import *
import json


def open_json():
    """Open and close the jsonfile acting as database."""
    a_file = open('db_files/bank.json', 'r')
    json_object = json.load(a_file)
    a_file.close()
    return json_object


def get_account_number():
    """Return a unique integer to be account_number."""
    number_list = []
    data = open_json()
    for d in data['bank']['customers']:
        for accounts in d['accounts']:
            if accounts:
                number_list.append(accounts['account_number'])
    return number_list[-1] + 1


def search_for_customer():
    """Take user input first and last name and gets that user."""
    data = open_json()
    print('Enter customer name: ')
    name = f_input()
    for data in data['bank']['customers']:
        if data['name'] == name:
            divider()
            print(data)
            divider()


def show_all_customers():
    """Show all the customer."""
    data = open_json()
    for data in data['bank']['customers']:
        print(data)
        divider()


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
        data['bank']['customers'].append(insert_dict)
        file.seek(0)
        json.dump(data, file, indent=2)


def add_account_to_customer():
    """Add new bank account to an existing customer."""
    insert_dict = {}
    print('Enter you name: ')
    name = f_input()
    print('Enter currency: ')
    currency = f_input()
    print('Enter amount: ')
    amount = f_input()
    insert_dict['account_number'] = get_account_number()
    insert_dict['currency'] = currency
    insert_dict['amount'] = amount
    json_object = open_json()
    for data in json_object['bank']['customers']:
        if data['name'] == name:
            data['accounts'].append(insert_dict)
            a_file = open("db_files/bank.json", "w")
            json.dump(json_object, a_file, indent=2)
            a_file.close()


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
