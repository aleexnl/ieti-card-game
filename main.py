from config import system


def main():
    system.checkSystem()  # Needed to initiate colorama in case we are using Windows
    print(system.sysMsg + 'Seaching database...')
    databaseConnection = system.checkDatabase()


main()
