import sqlite3
from os import path, name
from colorama import init, deinit, Fore, Style

sysMsg = Style.BRIGHT + Fore.BLUE + '[SYSTEM] ' + Style.RESET_ALL
infMsg = Style.BRIGHT + Fore.GREEN + '[INFO] ' + Style.RESET_ALL
errMsg = Style.BRIGHT + Fore.RED + '[ERROR] ' + Style.RESET_ALL
warMsg = Style.BRIGHT + Fore.YELLOW + '[WARNING] ' + Style.RESET_ALL
usrMsg = Style.BRIGHT + Fore.CYAN + '[USER]: ' + Style.RESET_ALL

database = None  # Variable to store the database connection.


def check_system():
    """
    Function to check the system where the script is running.
    """
    if name == 'nt':  # Checks if system is Windows.
        init()  # Execute colorama in windows.


def check_database():
    global database
    """
    Function to check if the database file exists in the
    specified folder.
    """
    if path.exists('database.db'):
        print(infMsg + "Found database")
        print(sysMsg + "Connecting...")
        database = database_connect()  # return the value of the database connection
    else:
        print(errMsg + "Database not found!")
        print(warMsg + "Exiting...")
        if name == 'nt':
            deinit()
        exit()


def database_connect():
    """
    Function to establish the database connection with SQLite3.
    """
    db = sqlite3.connect('database.db')
    print(infMsg + "Successfully connected to database")
    return db


def check_option(option, menu):
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


def exec_query(db, query):
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()
