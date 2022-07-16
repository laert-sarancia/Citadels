from game.player import Player
from game.building import Building
from game.data_base import DB

BUILDINGS = "buildings"


class Game:
    base = DB()

    def __init__(self, number_of_players):
        self.max_building_amount = 8
        self.game_end = False
        self.number_of_players = number_of_players
        self.dict_of_players = dict()
        self.free_drawings = self.get_drawings()
        self.used_drawings = list()

    def set_players(self):
        for i in range(self.number_of_players):
            name = f"Player{i}"
            self.dict_of_players.update({name: Player})  # ToDo add class Player

    def game_loop(self):
        while not self.game_end:
            value = input("End game? Y/N")
            if value.lower() == "y":
                break

    def get_drawings(self) -> list:
        """
        this method gets all drawings from DB and saves them as a list of objects
        :return: list_of_drawings
        """
        list_of_drawings = list()
        all_d = self.base.all_select(BUILDINGS)
        for building in all_d:
            list_of_drawings.append(Building(*building))
        return list_of_drawings


if __name__ == "__main__":
    print("This is internal file. Try to use 'start.py'")
