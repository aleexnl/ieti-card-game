import sqlite3
from os import path
from platform import system
from colorama import init, deinit, Fore, Style

sysMsg = Fore.BLUE + '[SYSTEM] ' + Style.RESET_ALL
infMsg = Fore.GREEN + '[INFO] ' + Style.RESET_ALL
errMsg = Fore.RED + '[ERROR] ' + Style.RESET_ALL


def checkSystem():
    if system() == 'Windows':
        init()


def checkDatabase():
    if path.exists('database.db'):
        print(infMsg + "Found database, connecting...")
        return databaseConnect()
    else:
        print(errMsg + "Database not found. Exiting")
        if system() == 'Windows':
            deinit()
        exit()


def databaseConnect():
    db = sqlite3.connect('database.db')
    print(sysMsg + "Successfully Connected to database")
    return db
