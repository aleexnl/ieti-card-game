import functions.sql
from . import system
from colorama import Style, Fore


def load_user():
    pass


def create_user():
    """
    Function to create a new user in database.
    TODO: Add more string validation.
    """
    while True:
        print(system.infMsg + "Please, choose an username for the new user: ")
        username = str(input(system.usrMsg))
        functions.sql.insert_new_user(system.database, (username, 0)) if system.check_str_input(username) is True else next
        break


def delete_user():
    pass


def show_users():
    """
    Function to get users and points from the database.
    """
    result = functions.sql.exec_query(system.database, "SELECT username, points FROM users")
    print(Style.BRIGHT + Fore.MAGENTA + "Username", end="")
    print("Points".rjust(15) + Style.RESET_ALL)
    for row in result:
        print(str(row[0]).ljust(20), end="")
        print(row[1])
