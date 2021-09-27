"""Module to create a MySQL table with SQL Alchemy."""
from MySQL.db import Base, session
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Account(Base):
    """Class to create accounts table in MySQL database."""

    __tablename__ = 'accounts'

    account_id = sa.Column(sa.Integer, primary_key=True)
    currency = sa.Column(sa.String(45), nullable=False)
    amount = sa.Column(sa.Float, nullable=False)
    bank_id = sa.Column(sa.Integer, sa.ForeignKey('banks.bank_id'))
    customer_id = sa.Column(sa.Integer, sa.ForeignKey('customers.customer_id'))
    customer = relationship('Customer', back_populates='accounts')
    bank = relationship('Bank', back_populates='accounts')

    @classmethod
    def get_columns(cls):
        """Show all columns in Account table."""
        return [column.key for column in cls.__table__.columns]

    @classmethod
    def by_id(cls, accountid):
        """Show row in Account based on ID, with Sql Alchemy."""
        return session.query(Account).filter(Account.account_id == accountid).first()

    @classmethod
    def delete(cls, accountid):
        """Delete row in Account with account_id."""
        try:
            session.query(Account).filter(Account.account_id == accountid).delete()
            print(f'Account: {accountid} deleted')
            session.commit()
        except:
            print("rollback")
            session.rollback()

    @classmethod
    def insert_money(cls, customer, value):
        """Change the value in Account.amount."""
        for c_acc in customer.accounts:
            acc = session.query(Account).filter(Account.account_id == c_acc.account_id).first()
            setattr(acc, 'amount', acc.amount + value)
            session.commit()
            print(f'{value} {acc.currency} inserted to account. New balance: {acc.amount + value}')

    @classmethod
    def withdraw_money(cls, customer, value):
        """Change the value in Account.amount."""
        for c_acc in customer.accounts:
            acc = session.query(Account).filter(Account.account_id == c_acc.account_id).first()
            setattr(acc, 'amount', acc.amount - value)
            session.commit()
            print(f'{value} {acc.currency} withdrawal from account. New balance: {acc.amount - value}')

    @classmethod
    def add_account(cls, insert_dict):
        """Take a dict as input, unpack it and adds it to database."""
        try:
            row = Account(**insert_dict)
            session.add(row)
            session.commit()
        except:
            print("rollback")
            session.rollback()
            return None

    def __repr__(self):
        """How to represent the class."""
        return f'Account(Id={self.account_id}, Currency={self.currency}, Amount={self.amount},' \
               f'Customer={self.customer}, Customer_Id={self.customer_id}' \
               f' Bank={self.bank}, Bank_id={self.bank_id})'


