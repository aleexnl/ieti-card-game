import random
from lxml import etree

ns = etree.FunctionNamespace(None)  # Used with my_abs() to make the function usable in a XPath expresion.


class Card:
    """ The card object class definition, used to build the cards in a simple way and show them to the user. """
    def __init__(self, summon_points, card_type, name, description, attack, defense):
        self.name = name
        self.description = description
        self.card_type = card_type
        self.summon_points = summon_points
        self.attack_points = attack
        self.defense_points = defense

    def show_card(self):  # Method to show the user the card information.
        # TODO: Function trim() to erase \n in strings
        print("Cost: {} Type: {} Name: {} Atk: {} Def: {}"
              .format(self.summon_points, self.card_type, self.name, self.attack_points, self.defense_points))


@ns
def my_abs(context, number):  # Function used in the balanced_deck() XPath expresion to calculate the absolute number.
    if number < 0:
        return number * -1
    else:
        return number


def random_deck(deck):  # Function to create a random deck.
    cards = []
    random_numbers = []  # List of random numbers.
    if deck.xpath('count(//name)') < 20:  # Check if at least 20 cards exist.
        print('ERROR: No hay un minimo de 20 cartas.')
        return cards
    # This while will work until the random_numbers list reach 10 non-repeated random numbers in it.
    while len(random_numbers) != 10:
        random_number = random.randint(1, deck.xpath('count(//name)'))
        if random_number not in random_numbers:
            random_numbers.append(random_number)
    for number in random_numbers:  # TODO: Change the function random_deck() to use the same algorithm as the other ones
        card_info = deck.xpath("//card[" + str(number) + "]")
        name = deck.xpath("//card   [" + str(number) + "]/name")
        desc = deck.xpath("//card[" + str(number) + "]/description")
        atk = deck.xpath("//card[" + str(number) + "]/attack")
        defense = deck.xpath("//card[" + str(number) + "]/defense")
        card = Card(card_info[0].get('summonPoints'), card_info[0].get('type'),
                    name[0].text, desc[0].text, atk[0].text, defense[0].text)
        card.show_card()
        cards.append(card)
    return cards


def offensive_deck(deck):  # Function to create a offensive deck.
    cards = []
    if deck.xpath('count(//name)') < 20:  # Check if at least 20 cards exist.
        print('ERROR: No hay un minimo de 20 cartas.')
        return cards
    #  This for is used to build the XPath expression and go through the 5 posible attack stats in every card.
    for attack in range(5, -1, -1):
        selected_cards = deck.xpath('/PlayerConfig/deck/card[attack[.=' + str(attack) + ']]')
        for card in selected_cards:  # TODO: Build a function to cover the card object creation.
            if len(cards) == 10:
                return cards
            name = card.xpath("name")
            desc = card.xpath("description")
            atk = card.xpath("attack")
            defense = card.xpath("defense")
            card = Card(card.get('summonPoints'), card.get('type'),
                        name[0].text, desc[0].text, atk[0].text, defense[0].text)
            card.show_card()
            cards.append(card)


def defensive_deck(deck):  # Function to create a defensive deck.
    cards = []
    if deck.xpath('count(//name)') < 20:
        print('ERROR: No hay un minimo de 20 cartas.')
        return cards
    #  This for is used to build the XPath expression and go through the 5 posible defense stats in every card.
    for defense in range(5, -1, -1):
        selected_cards = deck.xpath('/PlayerConfig/deck/card[defense[.=' + str(defense) + ']]')
        for card in selected_cards:  # TODO: Build a function to cover the card object creation.
            if len(cards) == 10:
                return cards
            name = card.xpath("name")
            desc = card.xpath("description")
            atk = card.xpath("attack")
            defense = card.xpath("defense")
            card = Card(card.get('summonPoints'), card.get('type'),
                        name[0].text, desc[0].text, atk[0].text, defense[0].text)
            card.show_card()
            cards.append(card)


def balanced_deck(deck):  # Function to create balanced decks
    cards = []
    if deck.xpath('count(//name)') < 20:  # Check if at least 20 cards exist, if not return empty deck.
        print('ERROR: No hay un minimo de 20 cartas.')
        return cards
    # This for will iterate for each posible attack (0 to 5) and create a list variable with the cards that match
    # the XPath expresion.
    for number in range(0, 6, 1):
        selected_cards = deck.xpath('/PlayerConfig/deck/card'
                                    '[my_abs(number(attack)-number(defense))=' + str(number) + ']')
        # We will iterate with the card list and build a card object and after that, it will be appended to the cards
        # variable.
        for card in selected_cards:  # TODO: Build a function to cover the card object creation.
            if len(cards) == 10:  # Check if the deck has enough cards to end the function
                return cards
            name = card.xpath("name")
            desc = card.xpath("description")
            atk = card.xpath("attack")
            defense = card.xpath("defense")
            card = Card(card.get('summonPoints'), card.get('type'),
                        name[0].text, desc[0].text, atk[0].text, defense[0].text)
            card.show_card()
            cards.append(card)

def balanced_deck(deck):
    cards = []
    if deck.xpath('count(//name)') < 20:
        print('ERROR: No hay un minimo de 20 cartas.')
        return cards
    for attack in range(5, -1, -1):
        for defense in range(5, -1, -1):
            selected_card = deck.xpath('/PlayerConfig/deck/card[attack[.=' + str(attack) + ']]') and \
                            deck.xpath('/PlayerConfig/deck/card[defense[.=' + str(defense) + ']]')
            if len(cards) == 10:
                return cards
            name = card.xpath("name")
            desc = card.xpath("description")
            atk = card.xpath("attack")
            defense = card.xpath("defense")
            card = Card(card.get('summonPoints'), card.get('type'),
                        name[0].text, desc[0].text, atk[0].text, defense[0].text)
            cards.append(card)
