import sqlite3
from os import path
from platform import system
from colorama import Fore, Style, init, deinit

sysMsg = Fore.BLUE + '[SYSTEM] ' + Style.RESET_ALL
infMsg = Fore.GREEN + '[INFO] ' + Style.RESET_ALL
errMsg = Fore.RED + '[ERROR] ' + Style.RESET_ALL


def checkSystem():
    if system() == 'Windows':
        init()


def dbConnect():
    db = sqlite3.connect('config/database.db')
    print(sysMsg + "Successfully Connected to database")
    return db


def main():
    checkSystem()  # Needed to initiate colorama in case we are using Windows
    print(sysMsg + 'Seaching database...')
    if path.exists('/config/database.db'):
        print(infMsg + "Found database, connecting...")
        dbConnection = dbConnect()
    else:
        print(errMsg + "Database not found. Exiting")
        if system() == 'Windows':
            deinit()
        exit()


main()
