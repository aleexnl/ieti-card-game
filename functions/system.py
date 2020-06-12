import sqlite3
from os import path, name
from colorama import init, deinit, Fore, Style

sysMsg = Style.BRIGHT + Fore.BLUE + '[SYSTEM] ' + Style.RESET_ALL
infMsg = Style.BRIGHT + Fore.GREEN + '[INFO] ' + Style.RESET_ALL
errMsg = Style.BRIGHT + Fore.RED + '[ERROR] ' + Style.RESET_ALL
warMsg = Style.BRIGHT + Fore.YELLOW + '[WARNING] ' + Style.RESET_ALL
usrMsg = Style.BRIGHT + Fore.CYAN + '[USER]: ' + Style.RESET_ALL


def checkSystem():
    """
    Function to check the system where the script is running.
    """
    if name == 'nt':  # Checks if system is Windows.
        init()  # Execute colorama in windows.


def checkDatabase():
    """
    Function to check if the database file exists in the
    specified folder.
    """
    if path.exists('database.db'):
        print(infMsg + "Found database")
        print(sysMsg + "Connecting...")
        return databaseConnect()  # return the value of the database connection
    else:
        print(errMsg + "Database not found!")
        print(warMsg + "Exiting...")
        if name == 'nt':
            deinit()
        exit()


def databaseConnect():
    """
    Function to establish the database connection with SQLite3.
    """
    db = sqlite3.connect('database.db')
    print(infMsg + "Successfully connected to database" + "\n")
    return db


def checkOption(option, menu):
    """
    Function to check if the option given by the user exists in the menu.
    """
    if option.upper() == "Q":
        print(warMsg + "Exiting.")
        exit()
    elif option in menu:
        menu[option]()  # Call option
    else:
        print(warMsg + "Option not found, please input a valid option.")
