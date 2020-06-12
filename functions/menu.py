from . import system
from colorama import Style


def mainMenu():
    while True:
        print(system.infMsg + Style.BRIGHT +
              "SELECT AN OPTION:" + Style.RESET_ALL)
        print("[1]. Load an user")
        print("[2]. Create a new user")
        print("[3]. Delete an user")
        print("[4]. Show all users")
        print("[Q]. Quit")
        option = str(input(system.usrMsg))
        system.checkOption(option)
