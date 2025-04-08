class Animal:
    def __init__(self, name):
        self.name = name

    def action(self):
        return "walked!"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        return "woofl woofl"

    def action(self):
        return super().action()


lola = Animal("Lola Animal")
assert lola.name == "Lola Animal"  # True
assert isinstance(lola, Animal)  # True
lola = Dog("Lola Dog")
assert lola.name == "Lola Dog"  # True
assert isinstance(lola, Dog)
assert lola.action() == "walked!"
assert lola.bark() == "woofl woofl"
