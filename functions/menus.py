from colorama import Style
from . import system, menu_options


def user_menu():
    """User menu function. Shows option based on users."""
    menu = {"1": menu_options.load_user, "2": menu_options.create_user,
            "3": menu_options.delete_user, "4": menu_options.show_users}
    while True:
        print("\n" + system.infMsg + Style.BRIGHT + "Select an option:" + Style.RESET_ALL)
        print("1. Load an user")
        print("2. Create a new user")
        print("3. Delete an user")
        print("4. Show all users")
        print("Q. Quit")
        option = str(input(system.usrMsg))  # Input user option of the menu
        system.check_option(option, menu)  # Check option and menu options
