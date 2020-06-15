import functions.system as sys
import functions.menus as men


def main():
    """Main function. This function could change during develop."""
    sys.check_system()  # Needed to initiate colorama in case we are using Windows
    print(sys.sysMsg + 'Searching database...')
    sys.check_database()  # Call database connection
    men.user_menu()


main()
