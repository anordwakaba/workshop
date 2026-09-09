class pet:
    def __init__(self, name,animal_type,hunger, energy,):
        self.name = name
        self.animal_type = animal_type
        self.hunger = 5
        self.energy = 5

    def feed (self):
        if self.hunger > 0:
            self.hunger -= 1
            self.energy += 1
            print (f"{self.name} has been fed.")
        else:
            print(f"{self.name} is not hungry.")

    def play (self):
        if self.energy > 0:
            self.energy -= 1
            self.hunger += 1
            print(f"{self.name} is playing.")
        else:
            print(f"{self.name} is too tired to play.")

    def status (self):
        print(f"{self.name} is a {self.animal_type}")
        print(f"Hunger level: {self.hunger}")
        print(f"Energy level: {self.energy}")


Animal = pet("Buddy", "Dog", 5, 5)

Animal.status()
Animal.feed()
Animal.play()
Animal.status()
