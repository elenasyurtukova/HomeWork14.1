def test_category_init(category_1, category_2):
    assert category_1.name == "хлеб"
    assert category_1.description == "хлебобулочные изделия"
    assert len(category_1.products) == 3

    assert category_1.category_count == 2
    assert category_2.category_count == 2

    assert category_1.product_count == 6
    assert category_2.product_count == 6
