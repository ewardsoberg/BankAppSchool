"""All the functions from bank menu."""
from MySQL.UI.menu_function import menu
from MySQL.UI.ui_utils import *
from MySQL.BL import controller


def search_for_customer():
    """Take user input first and last name and gets that user."""
    print('Enter first name: ')
    f_name = f_input()
    print('Enter last name:')
    l_name = f_input()
    controller.search_for_customer(f_name=f_name, l_name=l_name)


def show_all_customers():
    """Show all the customer."""
    customers = controller.show_all_customers()
    for customer in customers:
        print(customer)


def register_new_customer():
    """Take a dict and creates a new customer."""
    insert_dict = {}
    for column in controller.get_customer_columns():
        if column != "customer_id":
            insert_dict[column] = input(f'{column}: ')
    divider()

    customer = controller.add_customer(insert_dict)


def add_account_to_customer():
    """Add new bank account to an existing customer."""
    insert_dict = {}
    for column in controller.get_account_columns():
        if column != "account_id":
            insert_dict[column] = input(f'{column}: ')
    divider()

    account = controller.add_account(insert_dict)


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
