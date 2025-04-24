import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


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


@pytest.fixture
def smartphone1():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")

@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

@pytest.fixture
def grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")