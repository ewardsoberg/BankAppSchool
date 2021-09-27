"""Repository to 'speak' with the account and customer models."""
from MySQL.db.models.customer import Customer
from MySQL.db.models.account import Account


def withdraw_money(c_id, amount):
    """Connect with the customer and account model to use class method withdraw_money from account."""
    cust = Customer.by_id(c_id)
    return Account.withdraw_money(customer=cust, value=amount)


def insert_money(c_id, amount):
    """Connect with the customer and account model to use class method insert_money from account."""
    cust = Customer.by_id(c_id)
    return Account.insert_money(customer=cust, value=amount)


def get_columns():
    """Connect with class method get_column in the account model."""
    return Account.get_columns()


def add_account(insert_dict):
    """Connect with class method add_account in the account model."""
    return Account.add_account(insert_dict)
