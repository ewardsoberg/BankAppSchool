"""Module to create a MySQL table with SQL Alchemy."""
from MySQL.db import Base, session
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Bank(Base):
    """Class to create banks table in MySQL database."""

    __tablename__ = 'banks'

    bank_id = sa.Column(sa.Integer, primary_key=True)
    bank_name = sa.Column(sa.String(100), nullable=False)
    accounts = relationship('Account', back_populates='bank')

    @classmethod
    def by_id(cls, bankid):
        """Show row in Bank based on ID, with Sql Alchemy."""
        return session.query(Bank).filter(Bank.bank_id == bankid).first()

    @classmethod
    def show_all_bank(cls):
        """Show all rows in Bank table, with Sql Alchemy."""
        return session.query(Bank).all()

    def __repr__(self):
        """How to represent the class."""
        return f'Bank(bank_id={self.bank_id}, bank_name={self.bank_name})'
