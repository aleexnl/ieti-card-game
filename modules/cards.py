import random


class Card:
    def __init__(self, summon_points, card_type, name, description, attack, defense):
        self.name = name
        self.description = description
        self.card_type = card_type
        self.summon_points = summon_points
        self.attack_points = attack
        self.defense_points = defense

    def show_card(self):
        print("Cost: {} Type: {} Name: {} Atk: {} Def: {}"
              .format(self.summon_points, self.card_type, self.name, self.attack_points, self.defense_points))


def random_deck(deck):
    cards = []
    random_numbers = []
    if deck.xpath('count(//name)') < 20:
        print('ERROR: No hay un minimo de 20 cartas.')
        return cards
    while len(random_numbers) != 10:
        random_number = random.randint(1, deck.xpath('count(//name)'))
        if random_number not in random_numbers:
            random_numbers.append(random_number)
    for number in random_numbers:
        card_info = deck.xpath("//card[" + str(number) + "]")
        name = deck.xpath("//card[" + str(number) + "]/name")
        desc = deck.xpath("//card[" + str(number) + "]/description")
        atk = deck.xpath("//card[" + str(number) + "]/attack")
        defense = deck.xpath("//card[" + str(number) + "]/defense")
        card = Card(card_info[0].get('summonPoints'), card_info[0].get('type'),
                    name[0].text, desc[0].text, atk[0].text, defense[0].text)
        cards.append(card)
    return cards


def offensive_deck(deck):
    cards = []
    if deck.xpath('count(//name)') < 20:
        print('ERROR: No hay un minimo de 20 cartas.')
        return cards
    for attack in range(5, -1, -1):
        selected_card = deck.xpath('/PlayerConfig/deck/card[attack[.=' + str(attack) + ']]')
        for card in selected_card:
            name = card.xpath("name")
            desc = card.xpath("description")
            atk = card.xpath("attack")
            defense = card.xpath("defense")
            card = Card(card.get('summonPoints'), card.get('type'),
                        name[0].text, desc[0].text, atk[0].text, defense[0].text)
            if len(cards)<10:
                cards.append(card)
    for card in cards:
        card.show_card()

def defensive_deck(deck):
    cards = []
    if deck.xpath('count(//name)') < 20:
        print('ERROR: No hay un minimo de 20 cartas.')
        return cards
    for defense in range(5, -1, -1):
        selected_card = deck.xpath('/PlayerConfig/deck/card[defense[.=' + str(defense) + ']]')
        for card in selected_card:
            name = card.xpath("name")
            desc = card.xpath("description")
            atk = card.xpath("attack")
            defense = card.xpath("defense")
            card = Card(card.get('summonPoints'), card.get('type'),
                        name[0].text, desc[0].text, atk[0].text, defense[0].text)
            if len(cards)<10:
                cards.append(card)
    for card in cards:
        card.show_card()
