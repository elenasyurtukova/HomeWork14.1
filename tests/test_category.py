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
