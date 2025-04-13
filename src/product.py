class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":
    prod_1 = Product("белый хлеб", "хлебобулочные изделия", 35.5, 10)

    print(prod_1.name)
    print(prod_1.description)
    print(prod_1.price)
    print(prod_1.quantity)
