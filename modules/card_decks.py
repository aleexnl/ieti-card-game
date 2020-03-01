def is_deck_valid(deck):  # Check if the deck has a minimum of 20 cards.
    if len(deck) < 20:
        return False
    else:
        return True


def balanced_deck(user_deck):
    cards = user_deck.xpath('//name')
    valid_deck = is_deck_valid(cards)
    if valid_deck is not True:
        return 'ERROR: No se han encontrado 20 cartas en el mazo especificado.'
    for card in range(len(cards)):
        print('carta nº: ', card + 1)
        print(cards[card].text)
