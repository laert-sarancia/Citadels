import random
# from building import Building
from pprint import pprint


class Player:

    def __init__(self, name: str, free_drawings: list, is_player: bool = False):
        self.name = name
        self.is_player = is_player
        self.free_drawings = free_drawings
        self.gold = 2
        self.drawings = list()
        self.buildings = list()
        self.role = None
        self.get_start_drawings()
        self.score = 0

    def get_start_drawings(self):
        for _ in range(4):
            self.drawings.append(self.free_drawings.pop(0))

    def add_score(self, n):
        self.score += n

    def sub_score(self, n):
        self.score -= n

    def get_gold(self, n: int):
        self.gold += n

    def take_gold(self, n: int):
        if self.gold < n:
            print("You don't have enough gold")
            return None
        self.gold -= n
        return n

    def get_rid(self, n):
        if self.is_player:
            for _ in range(n):
                for i, card in enumerate(self.drawings):
                    print("Your hand:")
                    print(f"{i}: {card.name}")
                a = input("Select card to drop:")
        else:
            a = random.randint(len(self.drawings))
        free_drawings = self.drawings.pop(a)
        return free_drawings


if __name__ == "__main__":
    print("This is internal file. Try to use 'start.py'")
