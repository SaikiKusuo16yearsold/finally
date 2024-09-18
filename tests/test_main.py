import pytest

from src.main import Category, Product


@pytest.fixture()
def products():
    return Product("cola", "вкусная", 500, 6)


@pytest.fixture()
def category():
    return Category("drinks", "for drink", ["cola", "fanta", "sprite"])


def test_init(products, category):
    assert products.name == "cola"
    assert products.description == "вкусная"
    assert category.name == 'drinks'
    assert category.description == "for drink"
    assert category.products == ["cola", "fanta", "sprite"]
    assert Product.count_products == 6
    assert Product.count_category == 3