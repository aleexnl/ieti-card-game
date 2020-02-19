# De l'interpret lxml importem etree y despres de lxml.etree importem DTDParseError
from lxml import etree
from lxml.etree import DTDParseError

# Esta funcion carga el DTD, si no lo consigue printara un mensaje de error.
def charge_dtd():
    try:
        dtd = etree.DTD('config/IETI_Card_Game.DTD')
    except DTDParseError:
        print('ERROR: IETI_Card_Game.DTD no encontrado en el directorio config')

# Esta funcion carga el XML, si no lo consigue printara un mensaje de error.
def charge_user_deck():
    try:
        user_deck = etree.parse('decks/myBaraja.xml')
    except OSError:
        print('ERROR:myBaraja.xml no encontrado en el directorio decks')
    finally:
        return user_deck
# try:
#     enemy_deck = etree.parse('decks/Enemigo.xml')
# except OSError:
#     print('ERROR: Enemigo.xml no encontrado en el directorio decks')

# if dtd.validate(user_deck) is True:
#     print('validation succesful')
