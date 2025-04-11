import json

from src.category import Category
from src.product import Product


def func_read_file_json(path: str) -> list[dict]:
    """функция: читает данные из json-файла пользовательских настроек"""
    try:
        with open(path, encoding="utf-8") as file:
            try:
                products = json.load(file)
                return products
            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []


def create_categories_from_json(data):
    """Функция создает объекты классов 'Категории' и 'Товары'"""
    categories = []
    for elem in data:
        products = []
        for product in elem["products"]:
            products.append(Product(**product))
        elem["products"] = products
        categories.append(Category(**elem))
    return categories


if __name__ == "__main__":
    data = func_read_file_json("../data/products.json")
    print(data)
    categories = create_categories_from_json(data)
    print(categories[1].name)
    print(categories[1].products)
