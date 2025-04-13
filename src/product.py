class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, params_dict):
        new_product = cls(**params_dict)
        return new_product


if __name__ == "__main__":
    prod_1 = Product.new_product({"name": "белый хлеб",
                                  "description": "хлебобулочные изделия",
                                  "price": 35.5,
                                  "quantity": 10})

    print(prod_1.name)
    print(prod_1.description)
    print(prod_1.price)
    print(prod_1.quantity)
    prod_1.price = 15.1
    print(prod_1.price)

