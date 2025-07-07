class Hero:
    def __init__(self, name: str, power_level: int, health: int):
        self.name = name
        self.power_level = power_level
        self.health = health

    def use_power(self) -> str:
        return f"{self.name} uses their power!"


# TODO: Implement the FlightHero and StrengthHero classes
class StrengthHero(Hero):
    def __init__(self, name: str, power_level: int, health: int, lifting_capacity: int):
        super().__init__(name, power_level, health)
        self.lifting_capacity = lifting_capacity

    def use_power(self) -> str:
        return f"{self.name} lifts {self.lifting_capacity} pounds!"


class FlightHero(Hero):
    def __init__(self, name: str, power_level: int, health: int, flight_speed: int):
        super().__init__(name, power_level, health)
        self.flight_speed = flight_speed

    def use_power(self) -> str:
        return f"{self.name} flies at {self.flight_speed} mph!"


# Don't change the code below
flight_hero = FlightHero("Superman", 10, 100, 1000)
strength_hero = StrengthHero("Hulk", 10, 100, 1000)

assert flight_hero.name == "Superman"
assert flight_hero.power_level == 10
assert flight_hero.health == 100
assert flight_hero.flight_speed == 1000
assert flight_hero.use_power() == "Superman flies at 1000 mph!"

assert strength_hero.name == "Hulk"
assert strength_hero.power_level == 10
assert strength_hero.health == 100
assert strength_hero.lifting_capacity == 1000
assert strength_hero.use_power() == "Hulk lifts 1000 pounds!"
