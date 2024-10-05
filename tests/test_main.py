import pytest

from src.main import Category, Product


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


@pytest.fixture()
def answer2():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    return product1 + product2


def test_init(products, answer, answer1, answer2):
    assert products.products == [
        "Samsung Galaxy S23 Ultra, 180000.0, Остаток: 5",
        "Iphone 15, 210000.0, Остаток: 8",
        "Xiaomi Redmi Note 11, 31000.0, Остаток: 14",
    ]
    assert str(answer1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт"
    assert answer == "Смартфоны 27 шт"
    assert answer2 == 2580000.0
