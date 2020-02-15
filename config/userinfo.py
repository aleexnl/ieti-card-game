from lxml import etree
from lxml.etree import DTDParseError

try:
    dtd = etree.DTD('IETI_Card_Game.DTD')
except DTDParseError:
    print('ERROR: IETI_Card_Game.DTD no encontrado en el directorio config')
try:
    user_deck = etree.parse('../decks/myBaraja.xml')
except OSError:
    print('ERROR:myBaraja.xml no encontrado en el directorio decks')
# try:
#     enemy_deck = etree.parse('../decks/Enemigo.xml')
# except OSError:
#     print('ERROR: Enemigo.xml no encontrado en el directorio decks')

if dtd.validate(user_deck) is True:
    print('validation succesful')
