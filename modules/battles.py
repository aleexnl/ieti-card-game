user_active_deck = []
enemy_active_deck = []


def player_vs_player(user_deck, enemy_deck):
    user_life, enemy_life = 10
    while user_life or enemy_life > 0:
-----------------------------------------------
        import random

        mesa = []
        mesaenemiga = []
        cards = [('n', 'p', 't', 3, 2, 5), ('n', 'p', 't', 3, 2, 4), ('n', 'p', 't', 3, 2, 3), ('n', 'p', 't', 3, 2, 2),
                 ('n', 'p', 't', 3, 2, 1)]
        ecards = [('n', 'p', 't', 3, 2, 5), ('n', 'p', 't', 3, 2, 4), ('n', 'p', 't', 3, 2, 3),
                  ('n', 'p', 't', 3, 2, 2), ('n', 'p', 't', 3, 2, 1)]
        Player = [10, 'allcards', 'cardshand', 'cardsontable', 5, 1]
        Enemy = [10, 'allcards', 'cardshand', 'cardsontable', 5, 1]
        sp = Player[4]
        esp = Enemy[4]
        while sp > 0:
            if sp == 5:
                n = random.randrange(1, 5)
                carta = cards[n]
                mesa.append(cards[random.randrange(1, 5)])
                sp = sp - carta[5]
                while sp > 0:
                    for i in range(len(cards)):
                        if sp < cards[i][5]:
                            continue
                        if sp == cards[i][5]:
                            carta = cards[i]
                            mesa.append(carta)
                            sp = sp - carta[5]
                        elif sp >= cards[i][5]:
                            carta = cards[i]
                            mesa.append(carta)
                            sp = sp - carta[5]
                    else:
                        break
                print(mesa)
                print(sp)
        while esp > 0:
            if esp == 5:
                n = random.randrange(1, 5)
                carta = ecards[n]
                mesaenemiga.append(carta)
                esp = esp - carta[5]
                while esp > 0:
                    for i in range(len(ecards)):
                        if esp == ecards[i][5]:
                            carta = ecards[i]
                            mesaenemiga.append(carta)
                            esp = esp - carta[5]
                        elif esp >= ecards[i][5]:
                            carta = ecards[i]
                            mesaenemiga.append(carta)
                            esp = esp - carta[5]
                print(mesaenemiga)
                print(esp)
-------------------------------------------

        pass


def player_vs_bot(user_deck):
    user_life, bot_life = 10


def player_vs_bot_league(user_deck):
    user_life, bot_1_life, bot_2_life, bot_3_life, bot_4_life, bot_5_life = 10
