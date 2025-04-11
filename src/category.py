from src.product import Product


class Category():
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

if __name__ == "__main__":
    prod_1 = Product("белый хлеб", "хлебобулочные изделия", 35.5, 10)
    prod_2 = Product("отрубной хлеб", "хлебобулочные изделия", 31.0, 5)
    prod_3 = Product("ржаной хлеб", "хлебобулочные изделия", 37.6, 7)
    category_1 = Category('хлеб', 'хлебобулочные изделия', [prod_1, prod_2, prod_3])
    print(category_1.name)
    print(category_1.description)
    print(category_1.products)
    print(category_1.category_count)
    print(category_1.product_count)