class Treasure:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name} (Value: {self.value})"

class Location :
    def __init__(self, name):
        self.name = name
        self.treasures = []

    def add_treasure(self, treasure):
        if isinstance(treasure, Treasure):
            self.treasures.append(treasure)
            print(f"{treasure.name} has been added to {self.name}.")
        else:
            print("Only treasures can be added to the location.")

    def show_treasures(self):
        print(f"Treasures at {self.name}:")
        for treasure in self.treasures:
            print(treasure)

class Player :
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.score = 0

    def collect_treasure(self, treasure):
        if isinstance(treasure, Treasure):
            self.inventory.append(treasure)
            self.score += treasure.value
            print(f"{self.name} collected {treasure.name}. Score: {self.score}")
        else:
            print("Only treasures can be collected.")

    def show_inventory(self):
        print(f"{self.name}'s Inventory:")
        for treasure in self.inventory:
            print(treasure)

gold_coin = Treasure("Gold Coin", 100)
diamond = Treasure("Diamond", 500)
ancient_artifact = Treasure("Ancient Artifact", 100)

cave = Location("Karura Cave")
beach = Location("Diani Beach")

cave.add_treasure(ancient_artifact)

beach.add_treasure(gold_coin)
cave.add_treasure(ancient_artifact)

player1 = Player("Adrian")

cave.show_treasures()
beach.show_treasures()
player1.collect_treasure(gold_coin)
player1.collect_treasure(diamond)
player1.collect_treasure(ancient_artifact)
player1.show_inventory()