import random
from pprint import pprint
import copy
from game.player import Player
from game.building import Building
from game.data_base import DB

BUILDINGS = "buildings"
NAMES = ["Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Schulz", "Hoffmann",
         "Schäfer", "Koch", "Bauer", "Richter", "Klein", "Wolf", "Schröder", "Neumann", "Schwarz", "Zimmermann",
         "Braun", "Krüger", "Hofmann", "Hartmann", "Lange", "Schmitt", "Werner", "Schmitz", "Krause", "Meier",
         "Lehmann", "Schmid", "Schulze", "Maier", "Köhler", "Herrmann", "König", "Walter", "Mayer", "Huber",
         "Kaiser", "Fuchs", "Peters", "Lang", "Scholz", "Möller", "Weiß", "Jung", "Hahn", "Schubert",
         "Vogel", "Friedrich", "Keller", "Günther", "Frank", "Berger", "Winkler", "Roth", "Beck", "Lorenz",
         "Baumann", "Franke", "Albrecht", "Schuster", "Simon", "Ludwig", "Böhm", "Winter", "Kraus", "Martin",
         "Schumacher", "Krämer", "Vogt", "Stein", "Jäger", "Otto", "Sommer", "Groß", "Seidel", "Heinrich",
         "Brandt", "Haas", "Schreiber", "Graf", "Schulte", "Dietrich", "Ziegler", "Kuhn", "Kühn", "Pohl",
         "Engel", "Horn", "Busch", "Bergmann", "Thomas", "Voigt", "Sauer", "Arnold", "Wolff", "Pfeiffer"]


class Game:
    base = DB()

    def __init__(self, number_of_players):
        self.roles = {1: "Assassin",
                      2: "Thief",
                      3: "Magician",
                      4: "King",
                      5: "Bishop",
                      6: "Merchant",
                      7: "Architect",
                      8: "Warlord"}
        self.open_roles = []
        self.hidden_roles = []
        self.max_building_amount = 8
        self.game_end = False
        self.number_of_players = number_of_players
        self.free_drawings = self.get_drawings()
        self.dict_of_players = {key: Player(self.set_name(), self.free_drawings) for key in range(number_of_players)}
        self.sequence = [i for i in range(self.number_of_players)]

    def set_name(self):
        return random.choice(NAMES)

    def set_player(self, name):
        self.dict_of_players[0].name = name
        self.dict_of_players[0].is_player = True

    def first_crown(self):
        r = random.randint(0, self.number_of_players-1)
        print(f"Set Crown to {r} player, who is {self.dict_of_players[r].name}")
        self.dict_of_players[r].role = "King"
        self.set_sequence()

    def set_sequence(self):
        for pl in self.dict_of_players:
            if self.dict_of_players[pl].role == "King":
                print("King is", self.dict_of_players[pl].name, pl)  # ToDo REMOVE after debug
                while self.sequence[0] != pl:
                    self.sequence.append(self.sequence.pop(0))

    def shuffle_roles(self):
        temp_roles = [i for i in range(1, len(self.roles) + 1)]
        self.open_roles, self.hidden_roles = [], []
        random.shuffle(temp_roles)
        # print(temp_roles, "Roles have been shuffled")  # ToDo REMOVE after debug
        self.hidden_roles.append(temp_roles.pop(0))
        if self.number_of_players == 5:
            self.open_roles.append(temp_roles.pop(0))
            print("Open role:", self.roles[self.open_roles[0]])  # ToDo REMOVE after debug
        elif self.number_of_players == 4:
            self.open_roles.append(temp_roles.pop(0))
            print("Open role:", self.roles[self.open_roles[0]])  # ToDo REMOVE after debug
            self.open_roles.append(temp_roles.pop(0))
            print("Open role:", self.roles[self.open_roles[1]])  # ToDo REMOVE after debug
        if 4 in self.open_roles:
            self.shuffle_roles()
        return temp_roles

    def choose_role(self):
        temp_roles = self.shuffle_roles()
        for pl in self.sequence:
            print(temp_roles, "Free roles")  # ToDo REMOVE after debug
            print(self.dict_of_players[pl].name)
            if len(temp_roles) == 1:
                temp_roles.append(self.hidden_roles[0])
            if self.dict_of_players[pl].is_player:
                for i, rl in enumerate(temp_roles):
                    print(i, self.roles[rl])
                a = int(input("Choose role:"))  # ToDo Check input type and range
            else:
                a = random.randint(0, len(temp_roles)-1)
            print("Choice is :", a)  # ToDo Remove after debug

            pop = temp_roles.pop(a)
            self.dict_of_players[pl].role = self.roles[pop]
            print(self.dict_of_players[pl].name, self.dict_of_players[pl].role)  # ToDo Remove after debug
        self.hidden_roles.append(*temp_roles)

    def call_of_king(self):
        pass

    def game_loop(self):
        while not self.game_end:
            self.set_sequence()
            self.choose_role()
            self.call_of_king()
            #   Action
            #   Build
            value = input("End game? Y/N")  # ToDo complete
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

    def show_statistics(self):
        for pl in self.dict_of_players:
            print(self.dict_of_players[pl].name,
                  len(self.dict_of_players[pl].buildings),
                  self.dict_of_players[pl].score)


if __name__ == "__main__":
    print("This is internal file. Try to use 'start.py'")
    new_game = Game(6)
    new_game.choose_role()
