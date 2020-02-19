# Importamos los archivos menus y userinfo
from modules import menus, userinfo

while True:
    if userinfo.user_deck_charged is False and userinfo.enemy_deck_charged is False:
        menus.inital_menu()
    elif userinfo.user_deck_charged is True and userinfo.enemy_deck_charged is False:
        menus.user_deck_charged()
    elif userinfo.user_deck_charged is False and userinfo.enemy_deck_charged is True:
        menus.enemy_deck_charged()
    elif userinfo.user_deck_charged is True and userinfo.enemy_deck_charged is True:
        menus.all_decks_charged()
