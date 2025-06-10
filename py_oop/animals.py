class Animal:
    count = 0

    def __init__(self, name, type):
        self.name = name
        self.type = type
        Animal.count += 1

    def __str__(self):
        return f"Hi, my name is {self.name} and I am a {self.type}."

    @classmethod
    def factory(cls, name: str = "", type: str = ""):
        return cls(name, type) if name and type else cls.default()

    @classmethod
    def default(cls):
        return cls("Simba", "Lion")


class Cat(Animal):
    def __init__(self, name):
        self.type = "Cat"
        super().__init__(name, self.type)

    def __str__(self):
        return f"Hi, my name is {self.name} and I am the best cat."

    @classmethod
    def default(cls):
        return cls("Thomas")


class Dog(Animal):
    def __init__(self, name):
        self.type = "Dog"
        super().__init__(name, self.type)

    def __str__(self):
        return f"Hi, my name is {self.name} and I am heroic doggy."

    @classmethod
    def default(cls):
        return cls("Sparky")


# lola = Dog("Lola")
# sky = Cat("Sky")
# sparky = Dog.default()
# tom = Cat.default()
# simba = Animal.default()
# print(lola)
# print(sky)
# print(sparky)
# print(tom)
# print(simba)
# print(Animal.count)

mrbarker = Animal.factory()
print(mrbarker)
