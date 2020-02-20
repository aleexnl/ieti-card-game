from lxml import etree
from lxml.etree import DTDParseError

dtd_charged = False
user_deck_charged = False
enemy_deck_charged = False


def charge_dtd():
    global dtd_charged
    try:
        dtd = etree.DTD('config/IETI_Card_Game.DTD')
        print('INFO: IETI_Card_Game.DTD cargado correctamente')
        dtd_charged = True
        return dtd
    except DTDParseError:
        print('ERROR: IETI_Card_Game.DTD no encontrado en el directorio config')


def charge_user_deck(dtd):
    global user_deck_charged
    try:
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
        except AttributeError:
            print('ERROR: No ha sido posible validar myBaraja.xml')
            user_deck_charged = False
    except OSError:
        print('ERROR: myBaraja.xml no encontrado en el directorio decks')


def charge_enemy_deck(dtd):
    global enemy_deck_charged
    try:
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
        except AttributeError:
            print('ERROR: No ha sido posible validar Enemigo.xml')
            enemy_deck_charged = False
    except OSError:
        print('ERROR: Enemigo.xml no encontrado en el directorio decks')


