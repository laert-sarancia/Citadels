import random
from building import Building


class Player:

    def __int__(self, free_drawings: list):
        self.gold = 2
        self.drawings = list()
        self.buildings = list()
        self.role = None
        self.name = random.choice()
        self.get_start_drawings(free_drawings)

    def get_start_drawings(self, free_drawings: list):
        for _ in range(4):
            self.drawings.append(free_drawings.pop(0))

    def get_gold(self, n: int):
        self.gold += n

    def take_gold(self, n: int):
        if self.gold < n:
            print("You don't have enough gold")
            return None
        self.gold -= n
        return n
