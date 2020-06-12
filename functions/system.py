import sqlite3
from os import path, name
from colorama import init, deinit, Fore, Style

sysMsg = Style.BRIGHT + Fore.BLUE + '[SYSTEM] ' + Style.RESET_ALL
infMsg = Style.BRIGHT + Fore.GREEN + '[INFO] ' + Style.RESET_ALL
errMsg = Style.BRIGHT + Fore.RED + '[ERROR] ' + Style.RESET_ALL
usrMsg = Style.BRIGHT + Fore.CYAN + '[USER]: ' + Style.RESET_ALL


def checkSystem():
    if name == 'nt':  # Checks if system is Windows
        init()


def checkDatabase():
    if path.exists('database.db'):
        print(infMsg + "Found database")
        print(sysMsg + "Connecting...")
        return databaseConnect()
    else:
        print(errMsg + "Database not found!")
        print(infMsg + "Exiting...")
        if name == 'nt':
            deinit()
        exit()


def databaseConnect():
    db = sqlite3.connect('database.db')
    print(infMsg + "Successfully connected to database" + "\n")
    return db


def checkOption(option):
    menuFunctions = {1: "Create a new User", 2: "Load User",
                     3: "Delete User", 4: "Show Users"}
    if option.upper() == "Q":
        print(sysMsg + "Exiting.")
        exit()
