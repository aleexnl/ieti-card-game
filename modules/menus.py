from modules import userinfo
# Definimos la funcion initial menu que nos mostrara por pantalla el primer menu que se le mostrara al usuario
def inital_menu():
    while True:
        print('1. Cargar cartas')
        print('2. Carga cartas Enemigo')
        print('3. Salir')
        print('ESCOJE UNA OPCIÓN: ', end='')
        try:
            opc = int(input())
            if opc not in range(1, 4):
                print('ERROR: Introduce una opcion en el menu')
        except ValueError:
            print('ERROR: Solo introduce numeros')

# Definimos una segunda variable que es el de cargar las cartas
def charged_cards_menu():
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


# def verifydeck():
#      try:
#          inital_menu()
#      except UnboundLocalError:
#          print("ATENCIÓ:XML no carga correctamente")
#
#      try:
#          charged_cards_menu()
#      except UnboundLocalError:
#          print("ATENCIÓ:XML no carga correctamente")
#
