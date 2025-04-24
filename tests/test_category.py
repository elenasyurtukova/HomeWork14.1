import pytest


def test_category_init(category_1, category_2):
    assert category_1.name == "хлеб"
    assert category_1.description == "хлебобулочные изделия"
    assert len(category_1.products_in_list) == 3

    assert category_1.category_count == 2
    assert category_2.category_count == 2

    assert category_1.product_count == 6
    assert category_2.product_count == 6


def test_category_products_property(category_1):
    category_1.products == (
        "белый хлеб, 35.5 руб. Остаток: 10 шт.\n"
        "отрубной хлеб, 31.0 руб. Остаток: 5 шт.\n"
        "ржаной хлеб, 37.6 руб. Остаток: 7 шт."
    )


def test_category_products_setter(category_1, product):
    assert len(category_1.products_in_list) == 3
    category_1.add_product = product
    assert len(category_1.products_in_list) == 4


def test_category_products_setter_error(category_1, product):
    with pytest.raises(TypeError):
        category_1.add_product = 10


def test_category_products_setter_smartphone(category_1, smartphone1):
    category_1.add_product = smartphone1
    assert category_1.products_in_list[-1].name == "Samsung Galaxy S23 Ultra"


def test_category_products_setter_grass(category_1, grass1):
    category_1.add_product = grass1
    assert category_1.products_in_list[-1].name == "Газонная трава"


def test_category_str(category_1, category_2):
    assert str(category_1) == "хлеб, количество продуктов: 22 шт."
    assert str(category_2) == "конфеты, количество продуктов: 32 шт."


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "дюшес"
    assert next(product_iterator).name == "птичье молоко"
    assert next(product_iterator).name == "желейные"

    with pytest.raises(StopIteration):
        next(product_iterator)
