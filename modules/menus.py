from modules import userinfo, cards, battles

dtd_file = userinfo.charge_dtd()  # Var to load the xml validator.
user_deck = None  # Var that contains user's deck xml dom.
enemy_deck = None  # Var that contains enemy's deck xml dom.


def init_menu():
    """Initial menu of the game."""
    global user_deck
    global enemy_deck
    while True:  # If one deck is charged, stop showing this menu to search other posible option.
        if userinfo.enemy_deck_charged or userinfo.user_deck_charged is True:
            break
        print('1. Cargar cartas')
        print('2. Carga cartas Enemigo')
        print('ESCOJE UNA OPCIÓN: ', end='')
        try:
            opc = int(input())
            if opc not in range(1, 3):  # Check if the input is in the range of the options.
                print('ERROR: Introduce una opcion en el menu')
            elif opc == 1:  # Load user's xml deck
                user_deck = userinfo.charge_deck(dtd_file, user='user')
            elif opc == 2:  # Load enemy's xml deck
                enemy_deck = userinfo.charge_deck(dtd_file, user='enemy')
            else:  # Other unexpected error
                print('ERROR: Seleccion no esperada. Contacta con el desarrollador.')
        except ValueError:
            print('ERROR: Solo introduce numeros')


def all_menu():
    """Full menu of the game, every option is available."""
    global user_deck
    global enemy_deck
    while True:
        print('1. Cargar cartas')
        print('2. Carga cartas Enemigo')
        print('3. Crear mazo aleatorio')
        print('4. Crear mazo ofensivo')
        print('5. Crear mazo defensivo')
        print('6. Crear mazo equilibrado')
        print('7. Crear mazo aleatorio Enemigo')
        print('8. Crear mazo ofensivo Enemigo')
        print('9. Crear mazo defensivo Enemigo')
        print('10. Crear mazo equilibrado Enemigo')
        print('11. Luchar Jugador vs Jugador')
        print('12. Luchar Jugador vs Bot (arcade)')
        print('13. Luchar Jugador vs Bot (liga)')
        print('ESCOJE UNA OPCIÓN: ', end='')
        try:
            opc = int(input())
            if opc not in range(1, 14):
                print('ERROR: Introduce una opcion en el menu')
            elif opc == 1:
                user_deck = userinfo.charge_deck(dtd_file, user='user')
            elif opc == 2:
                enemy_deck = userinfo.charge_deck(dtd_file, user='enemy')
            elif opc == 3:
                battles.user_active_deck = cards.random_deck(user_deck)
            elif opc == 4:
                battles.user_active_deck = cards.offensive_deck(user_deck)
            elif opc == 5:
                battles.user_active_deck = cards.defensive_deck(user_deck)
            elif opc == 6:
                battles.user_active_deck = cards.balanced_deck(user_deck)
            elif opc == 7:
                battles.enemy_active_deck = cards.random_deck(enemy_deck)
            elif opc == 8:
                battles.enemy_active_deck = cards.offensive_deck(enemy_deck)
            elif opc == 9:
                battles.enemy_active_deck = cards.defensive_deck(enemy_deck)
            elif opc == 10:
                battles.enemy_active_deck = cards.balanced_deck(enemy_deck)
            elif opc == 11:
                print('ERROR: Opción no disponible')
            elif opc == 12:
                print('ERROR: Opción no disponible')
            elif opc == 13:
                print('ERROR: Opción no disponible')
            else:
                print('ERROR: Seleccion no esperada. Contacta con el desarrollador.')
        except ValueError:
            print('ERROR: Solo introduce numeros')


def user_deck_charged():
    global user_deck
    global enemy_deck
    while True:
        if userinfo.enemy_deck_charged is True or len(battles.user_active_deck) == 10:
            break
        print('1. Cargar cartas')
        print('2. Carga cartas Enemigo')
        print('3. Crear mazo aleatorio')
        print('4. Crear mazo ofensivo')
        print('5. Crear mazo defensivo')
        print('6. Crear mazo equilibrado')
        print('ESCOJE UNA OPCIÓN: ', end='')
        # Si lo que printa el usuario no es un numero del 1 al 7 el programa mostrara un mensaje de error
        try:
            opc = int(input())
            if opc not in range(1, 7):
                print('ERROR: Introduce una opcion en el menu')
            # Si el usuario printa 1 cargara el mazo del usuario
            elif opc == 1:
                user_deck = userinfo.charge_deck(dtd_file, user='user')
            # Si el usuario printa 2 cargara el mazo del enemigo
            elif opc == 2:
                enemy_deck = userinfo.charge_deck(dtd_file, user='enemy')
            elif opc == 3:
                battles.user_active_deck = cards.random_deck(user_deck)
            elif opc == 4:
                battles.user_active_deck = cards.offensive_deck(user_deck)
            elif opc == 5:
                battles.user_active_deck = cards.defensive_deck(user_deck)
            elif opc == 6:
                battles.user_active_deck = cards.balanced_deck(user_deck)
            else:
                print('ERROR: Seleccion no esperada. Contacta con el desarrollador.')
        # Si se introduce un valor que no sea un numero el programa printara un mensaje de error
        except ValueError:
            print('ERROR: Solo introduce numeros')


def enemy_deck_charged():
    global user_deck
    global enemy_deck
    while True:
        if userinfo.user_deck_charged is True:
            break
        print('1. Cargar cartas')
        print('2. Carga cartas Enemigo')
        print('3. Crear mazo aleatorio Enemigo')
        print('4. Crear mazo ofensivo Enemigo')
        print('5. Crear mazo defensivo Enemigo')
        print('6. Crear mazo equilibrado Enemigo')
        print('ESCOJE UNA OPCIÓN: ', end='')
        # Si lo que printa el usuario no es un numero del 1 al 7 el programa mostrara un mensaje de error
        try:
            opc = int(input())
            if opc not in range(1, 7):
                print('ERROR: Introduce una opcion en el menu')
            # Si el usuario printa 1 cargara el mazo del usuario
            elif opc == 1:
                user_deck = userinfo.charge_deck(dtd_file, user='user')
            # Si el usuario printa 2 cargara el mazo del enemigo
            elif opc == 2:
                enemy_deck = userinfo.charge_deck(dtd_file, user='enemy')
            elif opc == 3:
                battles.enemy_active_deck = cards.random_deck(enemy_deck)
            elif opc == 4:
                battles.enemy_active_deck = cards.offensive_deck(enemy_deck)
            elif opc == 5:
                battles.enemy_active_deck = cards.defensive_deck(enemy_deck)
            elif opc == 6:
                battles.enemy_active_deck = cards.balanced_deck(enemy_deck)
            else:
                print('ERROR: Seleccion no esperada. Contacta con el desarrollador.')
        # Si se introduce un valor que no sea un numero el programa printara un mensaje de error
        except ValueError:
            print('ERROR: Solo introduce numeros')


def all_decks_charged():
    global user_deck
    global enemy_deck
    while True:
        if len(battles.user_active_deck) == 10:
            break
        print('1. Cargar cartas')
        print('2. Carga cartas Enemigo')
        print('3. Crear mazo aleatorio')
        print('4. Crear mazo ofensivo')
        print('5. Crear mazo defensivo')
        print('6. Crear mazo equilibrado')
        print('7. Crear mazo aleatorio Enemigo')
        print('8. Crear mazo ofensivo Enemigo')
        print('9. Crear mazo defensivo Enemigo')
        print('10. Crear mazo equilibrado Enemigo')
        print('ESCOJE UNA OPCIÓN: ', end='')
        try:
            opc = int(input())
            if opc not in range(1, 11):
                print('ERROR: Introduce una opcion en el menu')
            elif opc == 1:
                user_deck = userinfo.charge_deck(dtd_file, user='user')
            elif opc == 2:
                enemy_deck = userinfo.charge_deck(dtd_file, user='enemy')
            elif opc == 3:
                battles.user_active_deck = cards.random_deck(user_deck)
            elif opc == 4:
                battles.user_active_deck = cards.offensive_deck(user_deck)
            elif opc == 5:
                battles.user_active_deck = cards.defensive_deck(user_deck)
            elif opc == 6:
                battles.user_active_deck = cards.balanced_deck(user_deck)
            elif opc == 7:
                battles.enemy_active_deck = cards.random_deck(enemy_deck)
            elif opc == 8:
                battles.enemy_active_deck = cards.offensive_deck(enemy_deck)
            elif opc == 9:
                battles.enemy_active_deck = cards.defensive_deck(enemy_deck)
            elif opc == 10:
                battles.enemy_active_deck = cards.balanced_deck(enemy_deck)
            else:
                print('ERROR: Seleccion no esperada. Contacta con el desarrollador.')
        except ValueError:
            print('ERROR: Solo introduce numeros')


def no_pvp_menu():
    """Full menu of the game, every option is available."""
    global user_deck
    global enemy_deck
    while True:
        if len(battles.enemy_active_deck) == 10:
            break
        print('1. Cargar cartas')
        print('2. Carga cartas Enemigo')
        print('3. Crear mazo aleatorio')
        print('4. Crear mazo ofensivo')
        print('5. Crear mazo defensivo')
        print('6. Crear mazo equilibrado')
        print('7. Crear mazo aleatorio Enemigo')
        print('8. Crear mazo ofensivo Enemigo')
        print('9. Crear mazo defensivo Enemigo')
        print('10. Crear mazo equilibrado Enemigo')
        print('11. Luchar Jugador vs Bot (arcade)')
        print('12. Luchar Jugador vs Bot (liga)')
        print('ESCOJE UNA OPCIÓN: ', end='')
        try:
            opc = int(input())
            if opc not in range(1, 13):
                print('ERROR: Introduce una opcion en el menu')
            elif opc == 1:
                user_deck = userinfo.charge_deck(dtd_file, user='user')
            elif opc == 2:
                enemy_deck = userinfo.charge_deck(dtd_file, user='enemy')
            elif opc == 3:
                battles.user_active_deck = cards.random_deck(user_deck)
            elif opc == 4:
                battles.user_active_deck = cards.offensive_deck(user_deck)
            elif opc == 5:
                battles.user_active_deck = cards.defensive_deck(user_deck)
            elif opc == 6:
                battles.user_active_deck = cards.balanced_deck(user_deck)
            elif opc == 7:
                battles.enemy_active_deck = cards.random_deck(enemy_deck)
            elif opc == 8:
                battles.enemy_active_deck = cards.offensive_deck(enemy_deck)
            elif opc == 9:
                battles.enemy_active_deck = cards.defensive_deck(enemy_deck)
            elif opc == 10:
                battles.enemy_active_deck = cards.balanced_deck(enemy_deck)
            elif opc == 11:
                print('ERROR: Opción no disponible')
            elif opc == 12:
                print('ERROR: Opción no disponible')
            else:
                print('ERROR: Seleccion no esperada. Contacta con el desarrollador.')
        except ValueError:
            print('ERROR: Solo introduce numeros')
