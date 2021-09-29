"""Uses Python classes to fill the database with some random data."""
import random
from MySQL.db.models.bank import Bank as ModelBank
from MySQL.db.models.customer import Customer as ModelCustomer
from MySQL.db.models.account import Account as ModelAccount
import MySQL.db.data_generator.file_generator as gen
from MySQL.db import session, Base, engine


class Customer:
    """Fills the MySQL customers table with the help of this Customer class."""

    def __init__(self):
        """__init__ method for Customer."""
        self.first_name = gen.random_first_name('first_last_name.txt')
        self.last_name = gen.random_last_name('first_last_name.txt')

    def __repr__(self):
        """How to represent."""
        return (
            f'FirstName: {self.first_name}\n'
            f'FirstName: {self.last_name}')


class Bank:
    """Fills the MySQL banks table with the help of this Bank class."""

    def __init__(self):
        """__init__ method for Bank."""
        self.bank_name = gen.random_bank('bank_names.txt')

    def __repr__(self):
        """How to represent the class."""
        return f'Bank(bank_name={self.bank_name})'


class Account:
    """Fills the MySQL accounts table with the help of this Account class."""

    def __init__(self):
        """__init__ method for Account."""
        self.currency = gen.random_currency('currency.csv')
        self.amount = random.randint(0, 50_000_000)
        self.bank_id = 1
        self.customer_id = random.randint(1, 100)

    def __repr__(self):
        """How to represent."""
        return (f'Currency: {self.currency}, Amount: {self.amount}\n'
                f' BankId: {self.bank_id}, CustomerId: {self.customer_id}')


def init_db():
    Base.metadata.create_all(bind=engine)


def populate_db(model, data_dict):
    """session.add() to add data to database before commit."""
    print(data_dict)
    model_obj = model(**data_dict)
    session.add(model_obj)


def commit_db():
    """session.commit() to commit to database."""
    session.commit()


def populate_db_random(model, data_classes, amount=1):
    """Convert class ref to list if not list of class refs."""
    if not isinstance(data_classes, list):
        data_classes = [data_classes]

    for _ in range(amount):
        generated_data = random.choice(data_classes)()
        populate_db(model, generated_data.__dict__)
        commit_db()


def populate_database(generations=1):
    """Populate multiple tables in the database with the populate_db_random function."""
    for _ in range(generations):
        populate_db_random(ModelCustomer, Customer, 100)
        populate_db_random(ModelBank, Bank, 1)
        populate_db_random(ModelAccount, Account, 200)


def main():
    """To se the data in customer, bank, accounts before populate.

    Only run populate_database one time to fill the database with mock data.
    """
    customers = [Customer() for _ in range(100)]

    for c in customers:
        print(c.__dict__)

    banks = [Bank() for _ in range(30)]

    for b in banks:
        print(b.__dict__)

    accounts = [Account() for _ in range(200)]

    for a in accounts:
        print(a.__dict__)

#init_db()
populate_database()


if __name__ == '__main__':
    main()
