class Person():
    species = "Human"
    def __init__(self,name):
        self.name = name
    @classmethod
    def get_species(cls):
        """Returns value of species var"""
        print(cls.species)

class Player(Person):
    def __init__(self, name, p_type):
        super().__init__(name)
        self.type = p_type
        self.inventory = ["sword-1", "shield-1"]
        self.health = 100
        self.alive = True
        self.experience = 1000
        self.block_status = False
    
    def __str__(self):
        return f"""
        'name': {self.name},
        'type': {self.type},
        'health': {self.health},
        'alive': {self.alive},
        'xp': {self.experience},
        'block_status': {self.block_status}
        """

    def attack(self, opponent):
        self.block_status = False
        if opponent.block:
            opponent.taking_hit(2)
            self.experience += 2
        else:
            opponent.taking_hit()
            self.experience += 10
    
    def block(self, block_status):
        self.block_status = block_status
        
    def taking_hit(self, combo_value=10):
        self.health -= combo_value
        self.alive = self.health > 0
    
    def heal(self, extra_health):
        new_heath = self.health + extra_health
        self.health = 100  if new_heath > 100 else new_heath
    
    def set_alive(self):
        self.alive = True if self.health > 0 else False
    
    @classmethod
    def get_species(cls):
        return super().get_species()

player_one = Player("Mason", "Paladin")
player_two = Player("Big", "Paladin")

player_one.attack(player_two)
player_two.block(True)
player_one.attack(player_two)
player_one.block(True)
player_two.attack(player_one)
player_two.block(False)
print(f"P1: {player_one}")
print(f"P2: {player_two}")

player_one.block(True)
player_two.block(True)
player_two.attack(player_one)
player_one.attack(player_two)
player_two.attack(player_one)
player_one.attack(player_two)
player_two.attack(player_one)
player_one.attack(player_two)
print(f"P1: {player_one}")
print(f"P2: {player_two}")

player_one.species = "Android"

Player.get_species()
Person.get_species()
player_one.get_species()
print(player_one.species)
print(repr(player_one.get_species()))