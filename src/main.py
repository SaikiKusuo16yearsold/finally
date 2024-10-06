class Product:

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт"

    def __add__(self, other):
        if issubclass(type(other), self.__class__):
            return self.price * self.quantity + other.__price * other.quantity
        raise TypeError

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price

    @classmethod
    def new_product(cls, my_dict):
        return cls(
            my_dict["name"],
            my_dict["description"],
            my_dict["price"],
            my_dict["quantity"],
        )


class Category:
    count_category = 0
    count_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.count_category += 1
        Category.count_products += len(products)

    def __str__(self):
        counter = 0
        for i in self.__products:
            counter = counter + i.quantity
        return f"{self.name} {counter} шт"

    def add_product(self, product):
        if issubclass(type(product), Product) or issubclass(type(product), Smartphone) or issubclass(type(product),
                                                                                                     LawnGrass):
            self.__products.append(product)
            Category.count_products += 1
        else:
            raise TypeError

    @property
    def products(self):
        return [
            f"{product.name}, {product.price}, Остаток: {product.quantity}"
            for product in self.__products
        ]


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
