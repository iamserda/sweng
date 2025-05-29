class Product:
    def __init__(self, name, price=0):
        self.__name: str = name
        self.__price: float = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __str__(self):
        return "The {} retails for {} at our stores.".format(self.__name, self.__price)


product1 = Product("Apple iPhone 13 Pro", 1099)
print(product1)
product1.name = "Apple iPhone 14 Pro"
product1.price = 1199
print(product1)
