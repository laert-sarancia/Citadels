from Game import game

exit = False

def start() -> str:
    return input(  # ToDo extend description
        '''
        Welcome to The Citadels
        It's a German-style card game, designed by Bruno Faidutti
        The game was ported on PC by Andrey Zolotin
         
Enter your name:''')


def settings() -> int:
    n_pl = int(input("Set number of players"))
    return n_pl


def main_loop(name):
    game = 0
    global exit
    while not exit:
        game += 1
        print(f"Game #{game} started.")
        answer = input("Do you want to start again? Y/N:")
        if answer.lower() == "n":
            exit = True
    print(f"Goodbye, {name}!")


if __name__ == "__main__":
    name = start()
    main_loop(name)
