import random
from modules import cards

user_active_deck = []
enemy_active_deck = []


def summon_phase(deck, field, summon_points=5):
    """Function to execute the summoning phase."""
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


def target_phase():
    x = random.randint(1, 2)
    return x


def battle_phase(coin, player_1_hp, player_1_field, player_2_hp, player_2_field):
    if coin == 1:
        player = 'User'
        player_2 = 'Enemigo'
    else:
        player = 'Enemigo'
        player_2 = 'User'
    for card_number in range(len(player_1_field)):
        player_1_card = player_1_field[card_number]
        print('Va a atacar', player_1_card.name
              , 'de tipo', player_1_card.card_type
              , 'con ataque', player_1_card.attack_points)
        try:
            player_2_card = player_2_field[card_number]
            print(player_2_card.name, 'defenderá con una defensa de valor', player_2_card.defense_points)
            if player_1_card.card_type == 'infantry' and player_2_card.card_type == 'lancer':
                print(player_1_card.name, 'tiene una ventaja de tipo; su ataque será de'
                      , int(player_1_card.attack_points)*2)
                player_1_card.attack_points = int(player_1_card.attack_points)*2
            elif player_1_card.card_type == 'lancer' and player_2_card.card_type == 'chivalry':
                print(player_1_card.name, 'tiene una ventaja de tipo; su ataque será de'
                      , int(player_1_card.attack_points) * 2)
                player_1_card.attack_points = int(player_1_card.attack_points) * 2
            elif player_1_card.card_type == 'chivalry' and player_2_card.card_type == 'infantry':
                print(player_1_card.name, 'tiene una ventaja de tipo. Su ataque será de'
                      , int(player_1_card.attack_points) * 2)
                player_1_card.attack_points = int(player_1_card.attack_points) * 2
            else:
                print('No hay ventajas de tipo')
        except IndexError:
            print('¡Enemigo no tiene cartas para defender!')
            print('¡', player_1_card.name, 'hará un ataque directo!')
            player_2_hp -= int(player_1_card.attack_points)
            print(player_1_card.name, 'ha hecho', player_1_card.attack_points
                  , 'y ahora le quedan', player_2_hp, 'puntos de vida a', player_2)
    return player_1_hp, player_1_field, player_2_hp, player_2_field


def player_vs_player(user_deck, enemy_deck):
    """Function to do a player vs player battle."""
    user_life, enemy_life = 10, 10
    while user_life or enemy_life > 0:
        user_field, enemy_field = [], []
        user_field = summon_phase(user_deck, user_field)
        print('User ha invocado a las siguientes cartas:')
        for card in user_field:
            card.get_card()
        enemy_field = summon_phase(enemy_deck, enemy_field)
        print('Enemigo ha invocado a las siguientes cartas:')
        for card in enemy_field:
            card.get_card()
        coin = target_phase()
        if coin == 1:
            print('User atacará primero')
            user_life, user_field, enemy_life, enemy_field = \
                battle_phase(coin, user_life, user_field, enemy_life, enemy_field)
        else:
            print('Enemigo atacará primero')
        break


def player_vs_bot(user_deck):
    user_life, bot_life = 10, 10


def player_vs_bot_league(user_deck):
    user_life, bot_1_life, bot_2_life, bot_3_life, bot_4_life, bot_5_life = 10, 10, 10, 10, 10, 10
