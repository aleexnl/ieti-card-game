import random
from modules import cards

user_active_deck = []
enemy_active_deck = []


def summon_phase(deck, field, summon_points=5):
    while summon_points > 0:
        available_cards = 0
        random_card = random.randrange(0, 10)
        field.append(deck[random_card])
        del deck[random_card]
        summon_points -= int(field[0].summon_points)
        for card in deck:
            if int(card.summon_points) < summon_points:
                available_cards += 1
        else:
            if available_cards == 0:
                break
        return field


def player_vs_player(user_deck, enemy_deck):
    user_life, enemy_life = 10, 10
    user_field, enemy_field = [], []
    while user_life or enemy_life > 0:
        user_field = summon_phase(user_deck, user_field)
        enemy_field = summon_phase(enemy_deck, enemy_field)
        break


def player_vs_bot(user_deck):
    user_life, bot_life = 10, 10


def player_vs_bot_league(user_deck):
    user_life, bot_1_life, bot_2_life, bot_3_life, bot_4_life, bot_5_life = 10, 10, 10, 10, 10, 10
