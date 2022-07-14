import random
from Player import Player

class Game:
    max_building_amount = 8
    game_end = False

    def __int__(self, max_players=7):
        self.max_players = max_players
        self.dict_of_players = dict()
        self.free_drawings = self.get_drawings()

    def set_players(self):
        for i in range(self.max_players):
            name = f"Player{i}"
            self.dict_of_players.update({name: Player})  # ToDo add class Player

    def game_loop(self):
        while self.game_end:
            pass

    def get_drawings(self) -> list:
        """
        this method gets all drawings from DB and saves them as a list of objects
        :return: list_of_drawings
        """
        pass

