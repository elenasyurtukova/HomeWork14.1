import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


@pytest.fixture
def category_1():
    return Category(
        name="хлеб",
        description="хлебобулочные изделия",
        products=[
            Product("белый хлеб", "хлебобулочные изделия", 35.5, 10),
            Product("отрубной хлеб", "хлебобулочные изделия", 31.0, 5),
            Product("ржаной хлеб", "хлебобулочные изделия", 37.6, 7),
        ],
    )


@pytest.fixture
def category_2():
    return Category(
        name="конфеты",
        description="конфеты и шоколад",
        products=[
            Product("дюшес", "леденцы", 1.5, 10),
            Product("птичье молоко", "суфле", 10.0, 7),
            Product("желейные", "желе", 3.5, 15),
        ],
    )


@pytest.fixture
def product():
    return Product("дюшес", "леденцы", 1.5, 10)


@pytest.fixture
def product_iterator(category_2):
    return ProductIterator(category_2)
