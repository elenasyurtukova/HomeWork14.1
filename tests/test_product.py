import pytest

from src.product import Product


def test_product_init(product):
    assert product.name == "дюшес"
    assert product.description == "леденцы"
    assert product.price == 1.5
    assert product.quantity == 10


def test_product_new_product():
    product = Product.new_product(
        {"name": "белый хлеб", "description": "хлебобулочные изделия", "price": 35.5, "quantity": 10}
    )
    assert product.name == "белый хлеб"
    assert product.description == "хлебобулочные изделия"
    assert product.price == 35.5
    assert product.quantity == 10


def test_price_setter(capsys, product):
    product.price = -15.5
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == "Цена не должна быть нулевая или отрицательная"
    product.price = 15.5
    assert product.price == 15.5


def test_product_str(product):
    assert str(product) == "дюшес, 1.5 руб. Остаток: 10 шт."


def test_add_product(product):
    assert product + Product("птичье молоко", "суфле", 10.0, 7) == 85.0


def test_add_product_error(product, category_2):
    with pytest.raises(TypeError, match="Невозможно сложить объекты разных типов"):
        product + category_2
