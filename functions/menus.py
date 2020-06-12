from . import system, menu_options
from colorama import Style


def userMenu():
    menu = {"1": menu_options.loadUser, "2": menu_options.createUser,
            "3": menu_options.deleteUser, "4": menu_options.showUsers}
    while True:
        print(system.infMsg + Style.BRIGHT +
              "SELECT AN OPTION:" + Style.RESET_ALL)
        print("[1]. Load an user")
        print("[2]. Create a new user")
        print("[3]. Delete an user")
        print("[4]. Show all users")
        print("[Q]. Quit")
        option = str(input(system.usrMsg))  # Input user option of the menu
        # Check option and menu options
        system.checkOption(option, menu)
