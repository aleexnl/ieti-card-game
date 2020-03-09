# Importamos el archivo userinfo
from modules import userinfo, cards

dtd_file = userinfo.charge_dtd()
user_deck = None
user_active_deck = []
enemy_deck = None
enemy_active_deck = []


# Definimos la funcion initial menu que nos mostrara por pantalla el primer menu que se le mostrara al usuario
def init_menu():
    global user_deck
    global enemy_deck
    while True:
        # Si el mazo del usuario y la del enemigo son True salimos del bucle y printamos el 1r menu.
        if userinfo.enemy_deck_charged or userinfo.user_deck_charged is True:
            break
        print('1. Cargar cartas')
        print('2. Carga cartas Enemigo')
        print('ESCOJE UNA OPCIÓN: ', end='')
        # Hacemos un try y si la opcion no es 1, 2 o 3 printara un mensaje de error y lo volvera a preguntar.
        try:
            opc = int(input())
            if opc not in range(1, 3):
                print('ERROR: Introduce una opcion en el menu')
            # Si el usuario printa 1 cargara el mazo del usuario
            elif opc == 1:
                user_deck = userinfo.charge_deck(dtd_file, user='user')
            # Si el usuario printa 2 cargara el mazo del enemigo
            elif opc == 2:
                enemy_deck = userinfo.charge_deck(dtd_file, user='enemy')
            else:
                print('ERROR: Seleccion no esperada. Contacta con el desarrollador.')
        # Si se introduce un valor que no sea un numero el programa printara un mensaje de error
        except ValueError:
            print('ERROR: Solo introduce numeros')


# Esta funcion carga el menu entero
def all_menu():
    global user_deck
    global enemy_deck
    global user_active_deck
    global enemy_active_deck
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
        # Si lo que printa el usuario no es un numero del 1 al 14 el programa mostrara un mensaje de error
        try:
            opc = int(input())
            if opc not in range(1, 14):
                print('ERROR: Introduce una opcion en el menu')
            # Si el usuario printa 1 cargara el mazo del usuario
            elif opc == 1:
                user_deck = userinfo.charge_deck(dtd_file, user='user')
            # Si el usuario printa 2 cargara el mazo del enemigo
            elif opc == 2:
                enemy_deck = userinfo.charge_deck(dtd_file, user='enemy')
            elif opc == 3:
                user_active_deck = cards.random_deck(user_deck)
            elif opc == 4:
                user_active_deck = cards.offensive_deck(user_deck)
            elif opc == 5:
                user_active_deck = cards.defensive_deck(user_deck)
            elif opc == 6:
                user_active_deck = cards.balanced_deck(user_deck)
            elif opc == 7:
                enemy_active_deck = cards.random_deck(enemy_deck)
            elif opc == 8:
                enemy_active_deck = cards.offensive_deck(enemy_deck)
            elif opc == 9:
                enemy_active_deck = cards.defensive_deck(enemy_deck)
            elif opc == 10:
                enemy_active_deck = cards.balanced_deck(enemy_deck)
            elif opc == 11:
                print('ERROR: Opción no disponible')
            elif opc == 12:
                print('ERROR: Opción no disponible')
            elif opc == 13:
                print('ERROR: Opción no disponible')
            else:
                print('ERROR: Seleccion no esperada. Contacta con el desarrollador.')
        # Si se introduce un valor que no sea un numero el programa printara un mensaje de error
        except ValueError:
            print('ERROR: Solo introduce numeros')


# La siguiente funcion cargara parte del menu que tiene relacion con la opcion 1, la de cargar cartas del usuario
def user_deck_charged():
    global user_deck
    global enemy_deck
    global user_active_deck
    while True:
        if userinfo.enemy_deck_charged is True:
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
                user_active_deck = cards.random_deck(user_deck)
            elif opc == 4:
                user_active_deck = cards.offensive_deck(user_deck)
            elif opc == 5:
                user_active_deck = cards.defensive_deck(user_deck)
            elif opc == 6:
                user_active_deck = cards.balanced_deck(user_deck)
            else:
                print('ERROR: Seleccion no esperada. Contacta con el desarrollador.')
        # Si se introduce un valor que no sea un numero el programa printara un mensaje de error
        except ValueError:
            print('ERROR: Solo introduce numeros')


# La siguiente funcion cargara parte del menu que tiene relacion con la opcion 2, la de cargar cartas enemigo
def enemy_deck_charged():
    global user_deck
    global enemy_deck
    global enemy_active_deck
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
                enemy_active_deck = cards.random_deck(enemy_deck)
            elif opc == 4:
                enemy_active_deck = cards.offensive_deck(enemy_deck)
            elif opc == 5:
                enemy_active_deck = cards.defensive_deck(enemy_deck)
            elif opc == 6:
                enemy_active_deck = cards.balanced_deck(enemy_deck)
            else:
                print('ERROR: Seleccion no esperada. Contacta con el desarrollador.')
        # Si se introduce un valor que no sea un numero el programa printara un mensaje de error
        except ValueError:
            print('ERROR: Solo introduce numeros')


# Esta ultima funcion carga solo las opciones del menu de cargar las cartas, no las de lucha
def all_decks_charged():
    global user_deck
    global enemy_deck
    global user_active_deck
    global enemy_active_deck
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
        print('ESCOJE UNA OPCIÓN: ', end='')
        # Si lo que printa el usuario no es un numero del 1 al 11 el programa mostrara un mensaje de error
        try:
            opc = int(input())
            if opc not in range(1, 11):
                print('ERROR: Introduce una opcion en el menu')
            elif opc == 1:
                user_deck = userinfo.charge_deck(dtd_file, user='user')
            elif opc == 2:
                enemy_deck = userinfo.charge_deck(dtd_file, user='enemy')
            elif opc == 3:
                user_active_deck = cards.random_deck(user_deck)
            elif opc == 4:
                user_active_deck = cards.offensive_deck(user_deck)
            elif opc == 5:
                user_active_deck = cards.defensive_deck(user_deck)
            elif opc == 6:
                user_active_deck = cards.balanced_deck(user_deck)
            elif opc == 7:
                enemy_active_deck = cards.random_deck(enemy_deck)
            elif opc == 8:
                enemy_active_deck = cards.offensive_deck(enemy_deck)
            elif opc == 9:
                enemy_active_deck = cards.defensive_deck(enemy_deck)
            elif opc == 10:
                enemy_active_deck = cards.balanced_deck(enemy_deck)
            else:
                print('ERROR: Seleccion no esperada. Contacta con el desarrollador.')
        # Si se introduce un valor que no sea un numero el programa printara un mensaje de error
        except ValueError:
            print('ERROR: Solo introduce numeros')
