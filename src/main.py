class Product:

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт"

    def __add__(self, other):
        return self.price * self.quantity + other.__price * other.quantity

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

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.count_products += 1

    @property
    def products(self):
        return [
            f"{product.name}, {product.price}, Остаток: {product.quantity}"
            for product in self.__products
        ]


# if __name__ == 'main':
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

# print(str(product1))
#     print(str(product2))
#     print(str(product3))
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#     #
#     print(str(category1))
#     #
#     print(category1.products)
#
#     print(product1 + product2)
#     print(product1 + product3)
#     print(product2 + product3)
