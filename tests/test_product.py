def test_product_init(product):
    assert product.name == "дюшес"
    assert product.description == "леденцы"
    assert product.price == 1.5
    assert product.quantity == 10
