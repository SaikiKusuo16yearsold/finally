class Product:
    count_category = 0
    count_products = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.count_products += quantity


class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Product.count_category += len(products)
