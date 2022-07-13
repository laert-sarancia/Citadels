from Game import Game

exit = False

def start() -> str:
    return input(  # ToDo extend description
        '''Welcome to The Citadels
        Enter your name:''')


def settings() -> int:
    n_pl = int(input("Set number of players"))
    return n_pl


def main_loop(name):
    game = 0
    while not exit:
        game += 1
        print(f"Game #{game} started.")
        answer = int(input("Do you want to start again? Y\N:"))



if __name__ == "__main__":
    name = start()
    main_loop(name)
