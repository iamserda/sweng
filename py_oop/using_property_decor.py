# using property decorators


class Animal:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return f"Hi, I am {self.__name}!"

    def set_name(self, name):
        if name:
            self.__name = name
        return self

    def get_name(self):
        return self.__name


# This class is using @property decorators to
# provide a name property that where
# we can store and update the dog's name.
class Dog(Animal):
    def __init__(self, name):
        # Animal.__init__(self, name)
        # Animal.__init__(Dog, name)
        # super().__init__(name)
        super()

    def __str__(self):
        return f"Hi, I am {self.name} the dog!"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name:
            self.__name = new_name


# Testing:
spark = Animal("Spark")
print(spark)
spark.set_name("Sparktacus")
print(spark)

lola = Dog("Lola")
lola.name = "Lola Marti"
print(lola)
lola.name = "Lola Martinez"
print(lola)

# print(lola.get_name())  # Error
lola.set_name("Lolita del Pueblo")
print(lola)  # Hi, I am Lola Martinez the dog!
# the name from @property, and setter.name
# ARE NOT the same self.__name
print(lola.name)  # property decorator
print(lola.get_name())  # self.__name in Animal
