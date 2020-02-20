# Importamos los archivos menus y userinfo
from modules import menus, userinfo

while True:
    if userinfo.user_deck_charged is False and userinfo.enemy_deck_charged is False:
        menus.inital_menu()
    # Comprobamos que ninguno de los dos mazos este cargado, y printamos por pantalla el primer menu que permite cargar
    # ambos mazos
    elif userinfo.user_deck_charged is True and userinfo.enemy_deck_charged is False:
        menus.user_deck_charged()
    # Si el usuario carga sus cartas aparecera un nuevo menu que a parte de las opciones anteriores nos da la
    # posibilidad, de crear un mazo.
    elif userinfo.user_deck_charged is False and userinfo.enemy_deck_charged is True:
        menus.enemy_deck_charged()
    # Por el contario si el usuario a decidido cargar primero las cartas del enemigo, nos apareceran las opciones de
    # crear mazos para el enemigo,
    elif userinfo.user_deck_charged is True and userinfo.enemy_deck_charged is True:
        menus.all_decks_charged()
# I finalmente si todas las cartas estan cargadas y esxisten los dos mazos, usuario y enemigo, podemos acceder a
# todas las opciones del menu, incluidas las de lucha.
