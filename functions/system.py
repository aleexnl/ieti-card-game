import sqlite3
from os import path, name
from colorama import init, deinit, Fore, Style

sysMsg = Style.BRIGHT + Fore.BLUE + '[SYSTEM] ' + Style.RESET_ALL
infMsg = Style.BRIGHT + Fore.GREEN + '[INFO] ' + Style.RESET_ALL
errMsg = Style.BRIGHT + Fore.RED + '[ERROR] ' + Style.RESET_ALL


def checkSystem():
    if name == 'nt':  # Checks if system is Windows
        init()


def checkDatabase():
    if path.exists('database.db'):
        print(infMsg + "Found database, connecting...")
        return databaseConnect()
    else:
        print(errMsg + "Database not found. Exiting")
        if name == 'nt':
            deinit()
        exit()


def databaseConnect():
    db = sqlite3.connect('database.db')
    print(sysMsg + "Successfully connected to database")
    return db
