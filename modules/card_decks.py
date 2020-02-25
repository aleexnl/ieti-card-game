def balanced_deck(user_deck):
    r = user_deck.xpath('//name')
    for i in range(len(r)):
        print(r[i].text)