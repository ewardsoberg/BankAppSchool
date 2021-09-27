"""Module to create a MySQL table with SQL Alchemy."""
from MySQL.db import Base, session
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Customer(Base):
    """Class to create customers table in MySQL database."""

    __tablename__ = 'customers'

    customer_id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String(45), nullable=False)
    last_name = sa.Column(sa.String(45), nullable=False)
    accounts = relationship('Account', back_populates='customer')

    @classmethod
    def all_customer(cls):
        """Show all rows in Customer table, with Sql Alchemy."""
        return session.query(Customer).all()

    @classmethod
    def by_id(cls, customerid):
        """Show rows with specific ID, with Sql Alchemy."""
        return session.query(Customer).filter(Customer.customer_id == customerid).first()

    @classmethod
    def delete(cls, customerid):
        """Delete rows with specific ID, with Sql Alchemy."""
        try:
            session.query(Customer).filter(Customer.customer_id == customerid).delete()
            print(f'Customer: {customerid} deleted')
            session.commit()
        except:
            print("rollback")
            session.rollback()

    @classmethod
    def search_by_name(cls, column_first='first_name', column_last='last_name', f_name=str, l_name=str):
        """Search based on first and last name, with Sql Alchemy."""
        return session.query(Customer).filter(getattr(Customer, column_first) == f_name) \
            .filter(getattr(Customer, column_last) == l_name).all()

    @classmethod
    def get_columns(cls):
        """Get all the columns in the table."""
        return [column.key for column in cls.__table__.columns]

    @classmethod
    def add_customer(cls, insert_dict):
        """Take a dict as input, unpack it and adds it to database."""
        try:
            row = Customer(**insert_dict)
            session.add(row)
            session.commit()
        except:
            print("rollback")
            session.rollback()
            return None

    def __repr__(self):
        """How to represent the class."""
        return f'Customer(Id: {self.customer_id}, FirstName: {self.first_name}, LastName: {self.last_name},' \
               f' Accounts: {", AccountID: ".join(str(acc.account_id)  +", Currency: "+ acc.currency +", Amount: "+ str(acc.amount) for acc in self.accounts)})'
