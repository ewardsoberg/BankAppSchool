"""Repository to 'speak' with the bank model."""
from MySQL.db.models.bank import Bank


def search_bank_id(bank_id):
    """Connect with class method by_id in the bank model."""
    return Bank.by_id(bank_id)


def show_all_banks():
    """Connect with class method show_all_banks in the bank model."""
    return Bank.show_all_bank()
