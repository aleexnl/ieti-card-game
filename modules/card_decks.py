def balanced_deck(user_deck):
    cards = user_deck.xpath('//card[1]//text()')
    print(cards)
    for card in range(len(cards)):
        print('carta nº: ', card + 1)
        print(cards[card])
