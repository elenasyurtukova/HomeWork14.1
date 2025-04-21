from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        quantity = 0
        for product in self.products_in_list:
            quantity += product.quantity
        return f"{self.name}, количество продуктов: {quantity} шт."

    @property
    def products_in_list(self):
        return self.__products

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @products.setter
    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1


if __name__ == "__main__":
    prod_1 = Product("белый хлеб", "хлебобулочные изделия", 35.5, 10)
    prod_2 = Product("отрубной хлеб", "хлебобулочные изделия", 31.0, 5)
    prod_3 = Product("ржаной хлеб", "хлебобулочные изделия", 37.6, 7)
    category_1 = Category("хлеб", "хлебобулочные изделия", [prod_1, prod_2, prod_3])
    print(category_1)

    prod_4 = Product("дарницкий хлеб", "хлебобулочные изделия", 39.6, 8)
    category_1.add_product = prod_4
    print(category_1.products)
    print(category_1.product_count)
