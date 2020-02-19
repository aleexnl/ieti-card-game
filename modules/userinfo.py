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
    except DTDParseError:
        print('ERROR: IETI_Card_Game.DTD no encontrado en el directorio config')
    if dtd_charged is True:
        return dtd


def charge_user_deck(dtd):
    global user_deck_charged
    try:
        user_deck = etree.parse('decks/myBaraja.xml')
        user_deck_charged = True
        return user_deck
    except OSError:
        print('ERROR: myBaraja.xml no encontrado en el directorio decks')
    if user_deck_charged is True:
        try:
            if dtd.validate(user_deck) is True:
                print('INFO: myBaraja.xml validado correctamente')
        except NameError:
            print('ERROR: No ha sido posible validar myBaraja.xml')
            user_deck_charged = False


def charge_enemy_deck(dtd):
    global enemy_deck_charged
    try:
        enemy_deck = etree.parse('decks/Enemigo.xml')
        enemy_deck_charged = True
        return enemy_deck
    except OSError:
        print('ERROR: Enemigo.xml no encontrado en el directorio decks')
    if enemy_deck_charged is True:
        try:
            if dtd.validate(enemy_deck) is True:
                print('INFO: Enemigo.xml validado correctamente')
        except NameError:
            print('ERROR: No ha sido posible validar Enemigo.xml')
            enemy_deck_charged = False

