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

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

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

    def __add__(self, other):
        if isinstance(other, Product):
            summ = self.price * self.quantity + other.price * other.quantity
            return summ
        else:
            raise ValueError("Невозможно сложить объекты разных типов")


if __name__ == "__main__":
    prod_1 = Product.new_product(
        {"name": "белый хлеб", "description": "хлебобулочные изделия", "price": 35.5, "quantity": 10}
    )
    prod_2 = Product.new_product(
        {"name": "отрубной хлеб", "description": "хлебобулочные изделия", "price": 31.0, "quantity": 5}
    )
    print(prod_1)
    # prod_1.price = 15.1
    # print(prod_1.price)
    print(prod_1 + prod_2)
