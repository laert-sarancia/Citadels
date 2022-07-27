from pprint import pprint

from game.building import Building
from game.data_base import DB
from game.game import Game, Proto

BUILDINGS = "buildings"
EXIT = False


def _get_drawings() -> list:
    """
    this method gets all drawings from DB and saves them as a list of objects
    :return: list_of_drawings
    """

    base = DB()
    list_of_drawings = list()
    all_d = base.all_select(BUILDINGS)
    for building in all_d:
        list_of_drawings.append(Building(*building))
    return list_of_drawings


def start() -> str:
    return input(  # ToDo extend description
        '''
        Welcome to The Citadels
        It's a German-style card game, designed by Bruno Faidutti
        The game was ported on PC by Andrey Zolotin
         
Enter your name:''')


def settings() -> int:
    available_amount = (4, 5, 6, 7)
    n_pl = input("Set number of players (4, 5, 6, 7):")
    try:
        while int(n_pl) not in available_amount:
            n_pl = int(input("Set number of players (4, 5, 6, 7):"))
        return int(n_pl)
    except ValueError:
        print("Please, input a number from range (4, 5, 6, 7)")
        settings()


def main_loop(name):
    game = 0
    global EXIT
    while not EXIT:
        game += 1
        print(f"Game #{game} started.")
        setting = settings()
        new_game = Game(setting)
        new_game.set_player(name)
        new_game.first_crown()
        new_game.game_loop()
        # new_game.show_statistics()

        answer = input("Do you want to start again? Y/N:")
        if answer.lower() == "n":
            EXIT = True
    print(f"Goodbye, {name}!")


if __name__ == "__main__":
    Proto.deck = _get_drawings()
    name = start()
    main_loop(name)
