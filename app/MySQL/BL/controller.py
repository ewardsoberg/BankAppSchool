"""Bridge between UI layer and Database layer."""
import MySQL.db.data_repository.customer_repo as cr
import MySQL.db.data_repository.account_repo as ar


def search_for_customer(f_name: str, l_name: str):
    """Connect with the customer_rep.py and return it to UI."""
    return cr.search_for_customer(f_name=f_name, l_name=l_name)


def show_all_customers():
    """Connect with the customer_rep.py and return it to UI."""
    return cr.show_all_customers()


def withdraw_money(c_id, amount):
    """Connect with the account_rep.py and return it to UI."""
    return ar.withdraw_money(c_id, amount)


def insert_money(c_id, amount):
    """Connect with the account_rep.py and return it to UI."""
    return ar.insert_money(c_id, amount)


def get_by_id(c_id):
    """Connect with the customer_rep.py and return it to UI."""
    return cr.get_by_id(c_id)


def get_customer_columns():
    """Connect with the customer_rep.py and return it to UI."""
    return cr.get_columns()


def get_account_columns():
    """Connect with the account_rep.py and return it to UI."""
    return ar.get_columns()


def update_table_column(column, value):
    """Connect with the customer_rep.py and return it to UI."""
    return cr.update_customer(column, value)


def add_customer(insert_dict):
    """Connect with the customer_rep.py and return it to UI."""
    return cr.add_customer(insert_dict)


def add_account(insert_dict):
    """Connect with the account_rep.py and return it to UI."""
    return ar.add_account(insert_dict)
