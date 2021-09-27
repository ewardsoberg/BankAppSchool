"""Repository to 'speak' with the customer model."""
from MySQL.db.models.customer import Customer


def search_for_customer(f_name: str, l_name: str):
    """Connect with class method search_by_name in the customer model."""
    print(Customer.search_by_name(f_name=f_name, l_name=l_name))


def show_all_customers():
    """Connect with class method all_customer in the customer model."""
    return Customer.all_customer()


def get_columns():
    """Connect with class method get_columns in the customer model."""
    return Customer.get_columns()


def get_by_id(c_id):
    """Connect with class method by_id in the customer model."""
    return Customer.by_id(customerid=c_id)


def update_customer(column, value):
    """Connect with class method update_customer in the customer model."""
    return Customer.update_customer(column, value)


def add_customer(insert_dict):
    """Connect with class method add_customer in the customer model."""
    return Customer.add_customer(insert_dict)

