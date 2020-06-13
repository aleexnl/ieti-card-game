from . import system
from colorama import Style, Fore


def load_user():
    pass


def create_user():
    pass


def delete_user():
    pass


def show_users():
    result = system.exec_query(
        system.database, "SELECT username, points FROM users")
    for row in result:
        print(Style.BRIGHT + Fore.MAGENTA + "User: " + Style.RESET_ALL + "{0}".format(row[0]), end="\t")
        print(Style.BRIGHT + Fore.MAGENTA + "Points: " + Style.RESET_ALL + "{0}".format(row[1]))
