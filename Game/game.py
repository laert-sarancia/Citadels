import random
from player import Player
from building import Building
import sqlite3


class Game:
    max_building_amount = 8
    game_end = False

    def __int__(self, max_players: int = 7):
        self.max_players = max_players
        self.dict_of_players = dict()
        self.free_drawings = self.get_drawings()
        self.used_drawings = list()

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
        conn = sqlite3.connect('buildings.db')
        cur = conn.cursor()
        # cur.execute("ВАШ-SQL-ЗАПРОС-ЗДЕСЬ;")
        # for building in db_buildings:
        #     self.free_drawings.append(
        #         Building(building["name"], building["price"], building["color"], building["properties"]))
        pass


if __name__ == "__main__":
    conn = sqlite3.connect('buildings.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS buildings(
        buildingid INT PRIMARY KEY,                          
        name TEXT,
        price INT,
        color TEXT,
        properties TEXT); 
        """)
    conn.commit()
    # cur.execute("""INSERT INTO buildings(
    #     buildingid, name, price, color, properties)
    #     VALUES('2', 'Port', '1', 'Green', '');""")
    # conn.commit()
    cur.execute("SELECT * FROM buildings;")
    one_result = cur.fetchone()
    print(one_result)
