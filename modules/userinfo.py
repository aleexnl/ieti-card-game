from lxml import etree
from lxml.etree import DTDParseError


def charge_dtd():
    try:
        dtd = etree.DTD('../config/IETI_Card_Game.DTD')
        print('INFO: IETI_Card_Game.DTD cargado correctamente')
        dtd_charged = True
    except DTDParseError:
        print('ERROR: IETI_Card_Game.DTD no encontrado en el directorio config')
        dtd_charged = False


def charge_user_deck(dtd):
    try:
        user_deck = etree.parse('../decks/myBaraja.xml')
        user_deck_charged = True
    except OSError:
        print('ERROR: myBaraja.xml no encontrado en el directorio decks')
        user_deck_charged = False
    if user_deck_charged is True:
        try:
            if dtd.validate(user_deck) is True:
                print('INFO: myBaraja.xml validado correctamente')
        except NameError:
            print('ERROR: No ha sido posible validar myBaraja.xml')


def charge_enemy_deck(dtd):
    try:
        enemy_deck = etree.parse('../decks/Enemigo.xml')
        enemy_deck_charged = True
    except OSError:
        print('ERROR: Enemigo.xml no encontrado en el directorio decks')
        enemy_deck_charged = False
    if enemy_deck_charged is True:
        try:
            if dtd.validate(enemy_deck) is True:
                print('INFO: Enemigo.xml validado correctamente')
        except NameError:
            print('ERROR: No ha sido posible validar Enemigo.xml')
