"""All the functions in customer_menu."""
from MySQL.UI.menu_function import menu
from MySQL.UI.ui_utils import *
from MySQL.BL import controller


def get_by_id():
    """Take customer id(int) as input and show that customer."""
    print('Enter you customer ID: ')
    c_id = f_input()
    return controller.get_by_id(c_id)


def search_for_account():
    """Take first and last name as input and show that customer."""
    print('Enter first name: ')
    f_name = f_input()
    print('Enter last name:')
    l_name = f_input()
    controller.search_for_customer(f_name=f_name, l_name=l_name)


def withdraw_money():
    """Take customer id as input and withdraw money from that customers account."""
    print('Enter Customer ID: ')
    c_id = f_input()
    print('Enter amount to withdraw: ')
    amount = float(f_input())
    controller.withdraw_money(c_id, amount)


def insert_money():
    """Take customer id as input and insert money to that customers account."""
    print('Enter Customer ID: ')
    c_id = f_input()
    print('Enter amount to insert: ')
    amount = float(f_input())
    controller.insert_money(c_id, amount)


def customer_menu():
    """Display all customer menu options."""
    menu({
        "1": {
            "info": "Search for account",
            "func": search_for_account
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