from game.game import Game

exit = False


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
        return n_pl
    except ValueError:
        print("Please, input a number from range (4, 5, 6, 7)")
        settings()


def main_loop(name):
    game = 0
    global exit
    while not exit:
        game += 1
        print(f"Game #{game} started.")
        setting = settings()
        new_game = Game(setting)
        new_game.game_loop()

        answer = input("Do you want to start again? Y/N:")
        if answer.lower() == "n":
            exit = True
    print(f"Goodbye, {name}!")


if __name__ == "__main__":
    name = start()
    main_loop(name)
