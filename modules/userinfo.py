#Importamos API para parsear el fitxero dtd y xml
from lxml import etree
from lxml.etree import DTDParseError
#Creamos tres variables
#dtd_charged la utilizamos vara validar el dtd
dtd_charged = False
#user_deck_charged la utilizamos para comprobar si carga la baraja del usuario
user_deck_charged = False
#enemy_deck_charged la utilizamos para comprobar si carga la baraja enemiga
enemy_deck_charged = False


#La función valida si el  dtd es correcto
def charge_dtd():
    #Creamos una variable global
    global dtd_charged
    #Si el dtd carga y es correcto devolvemos el dtd
    try:
        dtd = etree.DTD('config/IETI_Card_Game.DTD')
        print('INFO: IETI_Card_Game.DTD cargado correctamente')
        dtd_charged = True
        return dtd
    #Si el dtd no es correcto le indicamos que el dtd no ha sido cargado correctamente
    except DTDParseError:
        print('ERROR: IETI_Card_Game.DTD no encontrado en el directorio config')

#La función valida la baraja del usuario
def charge_user_deck(dtd):
    #Creamos una variable global para nuestra baraja
    global user_deck_charged
    #Comprobamos si la baraja carga correctamente
    try:
        #Comprobamos que nuestra baraja cargue correctamente
        user_deck = etree.parse('decks/myBaraja.xml')
        user_deck_charged = True
        print('INFO: myBaraja.xml cargado correctamente')
        try:
            #Comprobamos que nuestra baraja carga con el dtd
            if dtd.validate(user_deck) is True:
                print('INFO: myBaraja.xml validado correctamente')
                #Devuelve nuestra baraja ya validada
                return user_deck
        #Creamos excepciones para indicar cuando hay errores al validar el dtd con el xml
        except NameError:
            print('ERROR: No ha sido posible validar myBaraja.xml')
            user_deck_charged = False
        except AttributeError:
            print('ERROR: No ha sido posible validar myBaraja.xml')
            user_deck_charged = False
    #La baraja no carga correctamente y mostramos el error conforme no aparece en el directorio selecionado
    except OSError:
        print('ERROR: myBaraja.xml no encontrado en el directorio decks')

#La función valida la baraja enemiga
def charge_enemy_deck(dtd):
    # Creamos una variable global para la baraja enemiga
    global enemy_deck_charged
    # Comprobamos si la baraja enemiga carga correctamente
    try:
        # Comprobamos que la baraja enimiga cargue correctamente
        enemy_deck = etree.parse('decks/Enemigo.xml')
        enemy_deck_charged = True
        print('INFO: Enemigo.xml cargado correctamente')
        try:
            # Comprobamos que la baraja enemiga carga con el dtd
            if dtd.validate(enemy_deck) is True:
                print('INFO: Enemigo.xml validado correctamente')
                return enemy_deck
        # Creamos excepciones para indicar cuando hay errores al validar el dtd con el xml
        except NameError:
            print('ERROR: No ha sido posible validar Enemigo.xml')
            enemy_deck_charged = False
        except AttributeError:
            print('ERROR: No ha sido posible validar Enemigo.xml')
            enemy_deck_charged = False
    # La baraja no carga correctamente y mostramos el error conforme no aparece en el directorio selecionado
    except OSError:
        print('ERROR: Enemigo.xml no encontrado en el directorio decks')


