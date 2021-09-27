"""Pre menu to enter customer or bank menu."""
from MySQL.UI.customer_menu import customer_menu
from MySQL.UI.bank_menu import bank_menu
from MySQL.UI.menu_function import menu


main_menus = {
    "1": {
        "info": "Customers menu",
        "func": customer_menu,
    },
    "2": {
        "info": "Banks menu",
        "func": bank_menu
    },
    "3": {
        "info": "Exit",
        "func": quit
    }
}


def main_menu():
    """Run the menu."""
    menu(main_menus)


if __name__ == "__main__":
    main_menu()