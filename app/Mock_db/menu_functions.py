"""Module for displaying and handling the menus."""


def menu(menu_dict):
    """Take the menu dicts and redirects to the chosen function in a specific menu."""
    running = True
    while running:
        present_menus(menu_dict)
        answer = input('>')
        if answer in menu_dict:
            func = menu_dict[answer].get("func", lambda: None)
            func()
        else:
            print("exiting menu")
            running = False


def present_menus(menu_dict):
    """Display the menus and the different choices you can make."""
    for key, d in menu_dict.items():
        print(f'{key}) {d.get("info", "no description")}')
    print("-" * 20)

