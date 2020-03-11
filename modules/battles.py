import random
from modules import cards

user_active_deck = []
enemy_active_deck = []


def summon_phase(deck, field, summon_points=5):
    random_card = random.randrange(0, 10)
    summon_points -= int(deck[random_card].summon_points)
    field.append(deck[random_card])
    while summon_points != 0:
        available_cards = []
        for card in deck:
            if summon_points - int(card.summon_points) >= 0:
                available_cards.append(card)
        if len(available_cards) == 0:
            break
        random_card = random.randrange(0, len(available_cards))
        summon_points -= int(available_cards[random_card].summon_points)
        field.append(available_cards[random_card])
    return field


def player_vs_player(user_deck, enemy_deck):
    user_life, enemy_life = 10, 10
    user_field, enemy_field = [], []
    while user_life or enemy_life > 0:
        user_field = summon_phase(user_deck, user_field)
        enemy_field = summon_phase(enemy_deck, enemy_field)


def player_vs_bot(user_deck):
    user_life, bot_life = 10, 10


def player_vs_bot_league(user_deck):
    user_life, bot_1_life, bot_2_life, bot_3_life, bot_4_life, bot_5_life = 10, 10, 10, 10, 10, 10
