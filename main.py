from modules import menus, userinfo
while True:
    # Infinite bucle to always shot menus after iterating with options in them.
    # This conditionals check if the decks are charged or not and depending on the boolean returned, it will show more
    # or less options to the user.
    if userinfo.user_deck_charged is False and userinfo.enemy_deck_charged is False:
        menus.init_menu()
    elif userinfo.user_deck_charged is True and userinfo.enemy_deck_charged is False:
        menus.user_deck_charged()
    elif userinfo.user_deck_charged is False and userinfo.enemy_deck_charged is True:
        menus.enemy_deck_charged()
    elif userinfo.user_deck_charged is True and userinfo.enemy_deck_charged is True:
        menus.all_decks_charged()
