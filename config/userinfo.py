from lxml import etree

dtd = etree.DTD('IETI_Card_Game.DTD')
user_deck = etree.parse('../decks/myBaraja.xml')

print(dtd.validate(user_deck))
