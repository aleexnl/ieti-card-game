from .system import errMsg, sysMsg, infMsg
from colorama import Style

options = ["Create a new User", "Load User", "Delete User", "Show User"]


def mainMenu():
    optionNum = 1
    print(Style.BRIGHT + "SELECT AN OPTION:" + Style.RESET_ALL)
    for option in options:
        print("%d. %s" % (optionNum, option))
        optionNum += 1
