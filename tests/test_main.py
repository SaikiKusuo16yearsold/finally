import pytest
import unittest
from src.main import Category, Product, Smartphone, LawnGrass


@pytest.fixture()
def products():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    return category1


@pytest.fixture()
def test_for_method_add_1():
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    variant_with_right_classes = smartphone1 + smartphone2
    return variant_with_right_classes


@pytest.fixture()
def imitation_smartphone_class():
    smartphone = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                            "S23 Ultra", 256, "Серый")
    return smartphone


@pytest.fixture()
def imitation_lawngrass_class():
    lawngrass = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    return lawngrass


@pytest.fixture()
def answer1():
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )

    return product


@pytest.fixture()
def answer():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    return str(category1)


# @pytest.fixture()
# def answer3():
#     product1 = Product(
#         "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
#     )
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2]
#     )
#     smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
#
#     category1.add_product(smartphone3)
#     return category1.count_products


@pytest.fixture()
def answer2():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    return product1 + product2


def test_init(products, answer, answer1, answer2, imitation_lawngrass_class, imitation_smartphone_class,
              test_for_method_add_1):
    assert products.products == [
        "Samsung Galaxy S23 Ultra, 180000.0, Остаток: 5",
        "Iphone 15, 210000.0, Остаток: 8",
        "Xiaomi Redmi Note 11, 31000.0, Остаток: 14",
    ]
    assert str(answer1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт"
    assert answer == "Смартфоны 27 шт"
    assert answer2 == 2580000.0
    assert imitation_smartphone_class.memory == 256
    assert imitation_smartphone_class.color == "Серый"
    assert imitation_smartphone_class.efficiency == 95.5
    assert imitation_smartphone_class.model == "S23 Ultra"
    assert imitation_lawngrass_class.country == "США"
    assert imitation_lawngrass_class.germination_period == "5 дней"
    assert imitation_lawngrass_class.color == "Темно-зеленый"
    assert test_for_method_add_1 == 2580000.0
    quantity_before_adding = products.count_products
    products.add_product(imitation_smartphone_class)
    products.add_product(imitation_lawngrass_class)
    # таким образом я проверю, в __products добавлены новые элементы
    assert products.count_products == quantity_before_adding + 2
