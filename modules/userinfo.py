from lxml import etree
from lxml.etree import DTDParseError

dtd_charged = False  # Global boolean to check if the validation dtd is successful charged in memory.
user_deck_charged = False  # Global boolean to check if the user xml is successful charged in memory.
enemy_deck_charged = False  # Global boolean to check if the enemy xml is successful charged in memory.


def charge_dtd():  # Function used to charge the xml dtd validator.
    global dtd_charged  # Charge the global variable to change its condition .
    # Try to charge the dtd, if not it will catch the exception and warn the user about.
    try:
        dtd = etree.DTD('config/IETI_Card_Game.DTD')
        print('INFO: IETI_Card_Game.DTD cargado correctamente')
        dtd_charged = True
        return dtd
    except DTDParseError:
        print('ERROR: IETI_Card_Game.DTD no encontrado en el directorio config')


def charge_deck(dtd, user):
    try:
        if user == 'user':
            global user_deck_charged
            user_deck = etree.parse('decks/myBaraja.xml')
            user_deck_charged = True
            print('INFO: myBaraja.xml cargado correctamente')
            try:
                if dtd.validate(user_deck) is True:
                    print('INFO: myBaraja.xml validado correctamente')
                    return user_deck
            except NameError:
                print('ERROR: No ha sido posible validar myBaraja.xml')
                user_deck_charged = False
                return None
            except AttributeError:
                print('ERROR: No ha sido posible validar myBaraja.xml')
                user_deck_charged = False
                return None
        elif user == 'enemy':
            global enemy_deck_charged
            enemy_deck = etree.parse('decks/Enemigo.xml')
            enemy_deck_charged = True
            print('INFO: Enemigo.xml cargado correctamente')
            try:
                if dtd.validate(enemy_deck) is True:
                    print('INFO: Enemigo.xml validado correctamente')
                    return enemy_deck
            except NameError:
                print('ERROR: No ha sido posible validar Enemigo.xml')
                enemy_deck_charged = False
                return None
            except AttributeError:
                print('ERROR: No ha sido posible validar Enemigo.xml')
                enemy_deck_charged = False
                return None
    except OSError:
        if user == 'user':
            print('ERROR: myBaraja.xml no encontrado en el directorio decks')
        elif user == 'enemy':
            print('ERROR: Enemigo.xml no encontrado en el directorio decks')
        return None
