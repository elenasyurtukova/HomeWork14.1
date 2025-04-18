from src.category import Category
from src.product import Product


class ProductIterator:

    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


if __name__ == "__main__":
    prod_1 = Product("белый хлеб", "хлебобулочные изделия", 35.5, 10)
    prod_2 = Product("отрубной хлеб", "хлебобулочные изделия", 31.0, 5)
    prod_3 = Product("ржаной хлеб", "хлебобулочные изделия", 37.6, 7)
    category_1 = Category("хлеб", "хлебобулочные изделия", [prod_1, prod_2, prod_3])
    print(category_1)
    iterator = ProductIterator(category_1)
    for product in iterator:
        print(product)
    print()
    for product in iterator:
        print(product)
