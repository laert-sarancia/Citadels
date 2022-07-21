class Building:

    def __init__(self, id, name: str, price: int, color: str, property: str):
        self.id = id
        self.name = name
        self.price = price
        self.color = color
        self.property = property

    def cemetery(self, warlord, victim, target_building):
        if warlord != victim and victim.gold > 0:
            if victim.player:
                response = input(f"Do you want to pick up {target_building.name} in hand? Y/N:")
                if response.lower() == "n":
                    return
            victim.take_gold(1)
            victim.buildings.remove(target_building)
            victim.drawings.apend(target_building)

    def fort(self):
        pass

    def the_university(self, owner):
        owner.score += 2

    def dragon_gate(self, owner):
        owner.score += 2

    def school_of_magic(self, owner):
        if owner.role == "King" or owner.role == "Bishop" or owner.role == "Merchant" or owner.role == "Warlord":
            owner.get_gold(1)

    def laboratory(self, owner):
        if owner.player:
            response = input(f"Do you want to get rid a card from hand and take 1 gold for that? Y/N:")
            if response.lower() == "n":
                return
            owner.get_rid(1)
        owner.get_gold(1)

    def observatory(self):
        pass

    def forge(self):
        pass

    def great_wall(self):
        pass

    def ghost_town(self):
        pass

    def library(self):
        pass

    def throne_room(self):
        pass

    def quarry(self):
        pass

    def museum(self):
        pass

    def factory(self):
        pass

    def ballroom(self):
        pass

    def belfry(self):
        pass

    def arsenal(self):
        pass

    def lighthouse(self):
        pass

    def the_park(self):
        pass

    def hospital(self):
        pass

    def archive(self):
        pass

    def almshouse(self):
        pass

    def imperial_treasury(self):
        pass

    def well_of_wishes(self):
        pass


if __name__ == "__main__":
    print("This is internal file. Try to use 'start.py'")
