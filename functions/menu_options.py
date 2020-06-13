from . import system
from colorama import Style, Fore


def load_user():
    pass


def create_user():
    while True:
        print(system.infMsg + "Please, choose an username for the new user: ")
        username = str(input(system.usrMsg))
        system.insert_new_user(system.database, (username, 0)) if system.check_str_input(username) is True else next
        break


def delete_user():
    pass


def show_users():
    """
    Function to get users and points from the database.
    """
    result = system.exec_query(system.database, "SELECT username, points FROM users")
    for row in result:
        print(Style.BRIGHT + Fore.MAGENTA + "User: " + Style.RESET_ALL + "{0}".format(row[0]), end="\t\t")
        print(Style.BRIGHT + Fore.MAGENTA + "Points: " + Style.RESET_ALL + "{0}".format(row[1]))
