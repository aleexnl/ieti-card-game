import sys
from os import path, name
from colorama import init, deinit, Fore, Style
from .sql import database_connect

sysMsg = Style.BRIGHT + Fore.BLUE + '[System] ' + Style.RESET_ALL
infMsg = Style.BRIGHT + Fore.GREEN + '[Info] ' + Style.RESET_ALL
errMsg = Style.BRIGHT + Fore.RED + '[Error] ' + Style.RESET_ALL
warMsg = Style.BRIGHT + Fore.YELLOW + '[Warning] ' + Style.RESET_ALL
usrMsg = Style.BRIGHT + Fore.CYAN + 'User: ' + Style.RESET_ALL

DB_CONNECTION = None  # Variable to store the database connection.


def check_system():
    """Function to check the system where the script is running."""
    if name == 'nt':  # Checks if system is Windows.
        init()  # Execute colorama in windows.


def check_database():
    """Function to check if the database file exists in the specified folder."""
    global DB_CONNECTION
    if path.exists('database.db'):
        print(infMsg + "Found database")
        print(sysMsg + "Connecting...")
        DB_CONNECTION = database_connect()  # return the value of the database connection
    else:
        print(errMsg + "Database not found!")
        print(warMsg + "Exiting...")
        if name == 'nt':
            deinit()
        sys.exit()


def check_option(option, menu):
    """Function to check if the option given by the user exists in the menu."""
    if option.upper() == "Q":
        print(warMsg + "Exiting.")
        sys.exit()
    elif option in menu:
        menu[option]()  # Call option
    else:
        print(warMsg + "Option not found, please input a valid option.")


def check_str_input(string):
    """Function to string if the users input is a valid string. TODO: Add complete string validation."""
    if len(string) <= 0:
        print(errMsg + "No text provided.")
    else:
        return True


