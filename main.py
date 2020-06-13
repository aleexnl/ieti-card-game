from functions import system, menus
from os import system as os_system, name as os_name


def main():
    system.check_system()  # Needed to initiate colorama in case we are using Windows
    os_system('cls' if os_name == 'nt' else 'clear')
    print(system.sysMsg + 'Searching database...')
    system.check_database()  # Call database connection
    menus.user_menu()


main()
