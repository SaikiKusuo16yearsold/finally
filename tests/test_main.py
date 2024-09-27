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


def test_init(products):
    assert products.products == [
        "Samsung Galaxy S23 Ultra, 180000.0, Остаток: 5",
        "Iphone 15, 210000.0, Остаток: 8",
        "Xiaomi Redmi Note 11, 31000.0, Остаток: 14",
    ]
