import random
from game.game import Proto


class Player(Proto):

    def __init__(self, name: str, is_player: bool = False):
        self.name = name
        self.is_player = is_player
        self.gold = 2
        self.drawings = list()
        self.buildings = list()
        self.role = None
        self.get_start_drawings()
        self.score = 0
        self.income_gold = 2
        self.income_drawings = 2
        self.income_safe_drawings = 1

    def get_start_drawings(self):
        for _ in range(4):
            self.drawings.append(self.desk.pop(0))

    def add_score(self, n):
        self.score += n

    def sub_score(self, n):
        self.score -= n

    def get_gold(self, n: int):
        print(f"{self.name} gets {n} of gold")
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
            a = random.randint(0, len(self.drawings)-1)
        free_drawings = self.drawings.pop(a)
        return free_drawings

    def action(self):
        print(f"{self.name} do action")
        if self.is_player:
            a = input("Choose gold or card G/C:")
        else:
            if len(self.drawings) == 0 or self.gold > 6:
                a = "c"
            else:
                a = "g"
        # check buildings
        if a.lower() == "g":
            self.get_gold(self.income_gold)
        else:
            pool = []
            for _ in range(self.income_drawings):
                pool.append(self.desk.pop(0))
            if self.is_player:
                a = []
                for _ in range(self.income_safe_drawings):
                    for i, c in enumerate(pool):
                        print(i, c.name, c.price, c.color, c.property if c.property else "")
                    a.append(input("Choose card:"))
            else:
                for _ in range(self.income_safe_drawings):
                    self.ai_choice(pool)
            self.desk.append(*pool)

    def ai_choice(self, pool: list) -> list:
        """
        This method gets pool of cards and chooses better one
        :param pool: pool of cards
        :return: indexes of cards
        """
        a = []
        better_i = 0
        for _ in range(self.income_safe_drawings):
            better = pool[0]
            for i, c in enumerate(pool):
                buildings_names = [card.name for card in self.buildings]
                drawings_names = [card.name for card in self.drawings]
                if c.name not in a:
                    if c.name not in buildings_names and c.name not in drawings_names:
                        if better and c.price > better.price:
                            better_i = i
                            better = c
                    else:
                        better_i = random.randint(0, len(pool)-1)
                        better = pool[better_i]
            a.append(better_i)
        print(a, "favorite cards")
        return a


if __name__ == "__main__":
    print("This is internal file. Try to use 'start.py'")
