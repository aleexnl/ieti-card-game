import random

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
            if card not in field:
                if summon_points - int(card.summon_points) >= 0:
                    available_cards.append(card)
        if len(available_cards) == 0:
            break
        random_card = random.randrange(0, len(available_cards))
        summon_points -= int(available_cards[random_card].summon_points)
        field.append(available_cards[random_card])
    return field


def target_phase():
    """Function to decide the first to battle."""
    x = random.randint(1, 2)
    return x


def battle_phase(coin, player_1_hp, player_1_field, player_2_hp, player_2_field):
    """Function to execute the battle phase."""
    if coin == 1:
        player = 'User'
        player_2 = 'Enemigo'
    else:
        player = 'Enemigo'
        player_2 = 'User'
    for card_number in range(len(player_1_field)):
        player_1_card = player_1_field[card_number]
        print('Va a atacar', player_1_card.name, 'de tipo', player_1_card.card_type
              , 'con ataque', player_1_card.attack_points)
        try:
            player_2_card = player_2_field[card_number]
            print(player_2_card.name, 'defenderá con una defensa de valor', player_2_card.defense_points)
            if player_1_card.card_type == 'infantry' and player_2_card.card_type == 'lancer':
                print(player_1_card.name, 'tiene una ventaja de tipo; su ataque será de'
                      , int(player_1_card.attack_points) * 2)
                buff = True
            elif player_1_card.card_type == 'lancer' and player_2_card.card_type == 'chivalry':
                print(player_1_card.name, 'tiene una ventaja de tipo; su ataque será de'
                      , int(player_1_card.attack_points) * 2)
                buff = True
            elif player_1_card.card_type == 'chivalry' and player_2_card.card_type == 'infantry':
                print(player_1_card.name, 'tiene una ventaja de tipo. Su ataque será de'
                      , int(player_1_card.attack_points) * 2)
                buff = True
            else:
                print('No hay ventajas de tipo')
                buff = False
            print(player_1_card.name, 'va a atacar a', player_2_card.name)
            if buff is True:
                if int(player_2_card.defense_points) - (int(player_1_card.attack_points) * 2) >= 0:
                    print('¡', player_2_card.name, 'ha defendido con exito!')
                elif int(player_2_card.defense_points) - (int(player_1_card.attack_points) * 2) < 0:
                    print('¡', player_1_card.name, 'ha destruido a', player_2_card.name, '!')
                    player_2_hp -= abs(int(player_2_card.defense_points) - (int(player_1_card.attack_points) * 2))
                    print(player_1_card.name, 'ha inflingido',
                          abs(int(player_2_card.defense_points) - (int(player_1_card.attack_points) * 2)),
                          'puntos de daño')
                    print('A', player_2, 'le quedan', player_2_hp, 'puntos de vida')
                    player_2_field.remove(player_2_field[card_number])
                    if player_2_hp <= 0:
                        return player_1_hp, player_1_field, player_2_hp, player_2_field
            else:
                if int(player_2_card.defense_points) - int(player_1_card.attack_points) >= 0:
                    print('¡', player_2_card.name, 'ha defendido con exito!')
                elif int(player_2_card.defense_points) - int(player_1_card.attack_points) < 0:
                    print('¡', player_1_card.name, 'ha destruido a', player_2_card.name, '!')
                    player_2_hp -= abs(int(player_2_card.defense_points) - int(player_1_card.attack_points))
                    print(player_1_card.name, 'ha inflingido',
                          abs(int(player_2_card.defense_points) - int(player_1_card.attack_points)), 'puntos de daño')
                    print('A', player_2, 'le quedan', player_2_hp, 'puntos de vida')
                    player_2_field.remove(player_2_field[card_number])
                    if player_2_hp <= 0:
                        return player_1_hp, player_1_field, player_2_hp, player_2_field
        except IndexError:
            print(player_2, 'no tiene cartas para defender!')
            print('¡', player_1_card.name, 'hará un ataque directo!')
            player_2_hp -= int(player_1_card.attack_points)
            print(player_1_card.name, 'ha hecho', player_1_card.attack_points
                  , ' puntos de daño y ahora le quedan', player_2_hp, 'puntos de vida a', player_2)
            if player_2_hp <= 0:
                print('a', player_2, 'no le queda vida, gana', player)
                return player_1_hp, player_1_field, player_2_hp, player_2_field
    return player_1_hp, player_1_field, player_2_hp, player_2_field


def player_vs_player(user_deck, enemy_deck):
    """Function to do a player vs player battle."""
    user_life, enemy_life = 10, 10
    shift = 1
    while user_life and enemy_life > 0:
        print('Turno:', shift)
        print('Vida de usuario:', user_life)
        print('Vida de enemigo:', enemy_life)
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
            print('Fase de batalla de usuario')
            user_life, user_field, enemy_life, enemy_field = \
                battle_phase(coin, user_life, user_field, enemy_life, enemy_field)
            if enemy_life <= 0:
                break
            coin = 0
            print('Fase de batalla de enemigo')
            enemy_life, enemy_field, user_life, user_field = \
                battle_phase(coin, enemy_life, enemy_field, user_life, user_field)
            if user_life <= 0:
                break
        else:
            print('Enemigo atacará primero')
            print('Fase de batalla de enemigo')
            enemy_life, enemy_field, user_life, user_field = \
                battle_phase(coin, enemy_life, enemy_field, user_life, user_field)
            if user_life <= 0:
                break
            coin = 1
            print('Fase de batalla de usuario')
            user_life, user_field, enemy_life, enemy_field = \
                battle_phase(coin, user_life, user_field, enemy_life, enemy_field)
            if enemy_life <= 0:
                break
        shift += 1
    if enemy_life <= 0:
        print('¡A Enemigo no le quedan puntos de vida, gana User!')
    elif user_life <= 0:
        print('¡A User no le quedan puntos de vida, gana Enemigo!')


def player_vs_bot(user_deck, bot_deck):
    """Function to do a player vs bot battle."""
    user_life, bot_life = 10, 10
    shift = 1
    while user_life and bot_life > 0:
        print('Turno:', shift)
        print('Vida de usuario:', user_life)
        print('Vida del bot:', bot_life)
        user_field, bot_field = [], []
        user_field = summon_phase(user_deck, user_field)
        print('User ha invocado a las siguientes cartas:')
        for card in user_field:
            card.get_card()
        enemy_field = summon_phase(bot_deck, bot_field)
        print('El Bot ha invocado a las siguientes cartas:')
        for card in bot_field:
            card.get_card()
        coin = target_phase()
        if coin == 1:
            print('User atacará primero')
            print('Fase de batalla de usuario')
            user_life, user_field, bot_life, bot_field = \
                battle_phase(coin, user_life, user_field, bot_life, bot_field)
            if bot_life <= 0:
                break
            coin = 0
            print('Fase de batalla del Bot')
            bot_life, bot_field, user_life, user_field = \
                battle_phase(coin, bot_life, bot_field, user_life, user_field)
            if user_life <= 0:
                break
        else:
            print('Bot atacará primero')
            print('Fase de batalla de Bot')
            bot_life, bot_field, user_life, user_field = \
                battle_phase(coin, bot_life, bot_field, user_life, user_field)
            if user_life <= 0:
                break
            coin = 1
            print('Fase de batalla de usuario')
            user_life, user_field, bot_life, bot_field = \
                battle_phase(coin, user_life, user_field, bot_life, bot_field)
            if bot_life <= 0:
                break
        shift += 1
    if bot_life <= 0:
        print('¡Al Bot no le quedan puntos de vida, gana User!')
    elif user_life <= 0:
        print('¡A User no le quedan puntos de vida, gana Enemigo!')


def player_vs_bot_league(user_deck):
    """Function to do a player vs  5 bot battle (league mode)."""
    pass
