import random
from lxml import etree


class Card:
    def __init__(self, name, description, card_type, summon_points, attack, defense):
        self.name = name
        self.description = description
        self.card_type = card_type
        self.summon_points = summon_points
        self.attack_points = attack
        self.defense_points = defense

    def show_card(self):
        print("{} costs {} summon points. Has {} attack and {} defense."
              .format(self.name, self.summon_points, self.attack_points, self.defense_points))


def balanced_deck(deck):
    cards = deck.xpath('//name')
    for card in range(len(cards)):
        print('carta nº: ', card + 1)
        print(cards[card].text)
    # TODO: End balanced deck creator


def random_deck(deck):
    defined_deck = {}
    random_numbers = []
    if deck.xpath('count(//name)') < 20:
        print('ERROR: No hay un minimo de 20 cartas.')
        return defined_deck
    while len(random_numbers) != 10:
        random_number = random.randint(0, deck.xpath('count(//name)'))
        if random_number not in random_numbers:
            random_numbers.append(random_number)