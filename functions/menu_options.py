from colorama import Style, Fore
import functions.sql as sql
from . import system as sys


def load_user():
    """Function to load user from database."""
    while True:
        print(sys.infMsg + "Please, type an username to load: ")
        username = str(input(sys.usrMsg))
        if sys.check_str_input(username) is True:
            pass
        else:
            continue


def create_user():
    """Function to create a new user in database."""
    while True:
        print(sys.infMsg + "Please, choose an username for the new user: ")
        username = str(input(sys.usrMsg))
        if sys.check_str_input(username) is True:
            sql.insert_new_user(sys.DB_CONNECTION, (username.lower(), 0))
            break
        else:
            continue


def delete_user():
    """Function to delete users from database."""
    pass


def show_users():
    """Function to get users and points from the database."""
    result = sql.exec_query(sys.DB_CONNECTION, "SELECT username, points FROM users")
    print(Style.BRIGHT + Fore.MAGENTA + "Username", end="")
    print("Points".rjust(15) + Style.RESET_ALL)
    for row in result:
        print(str(row[0]).ljust(20), end="")
        print(row[1])
