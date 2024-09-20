import pytest

from src.main import Category, Product


@pytest.fixture()
def products():
    return Product("cola", "вкусная", 500, 6)


@pytest.fixture()
def category_1():
    return Category("drinks", "for drink", ["cola", "fanta", "sprite"])


@pytest.fixture()
def category_2():
    return Category("phones", "mobile phones", ["apple", "samsung", "xiaomi"])


def test_init(products, category_1, category_2):
    assert products.name == "cola"
    assert products.description == "вкусная"
    assert category_1.name == "drinks"
    assert category_1.description == "for drink"
    assert category_1.products == ["cola", "fanta", "sprite"]
    assert Category.count_products == 6
    assert Category.count_category == 2
