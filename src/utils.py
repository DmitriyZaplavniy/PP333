import json
from .models import Product, Category

def load_data_from_json(file_path: str) -> list:
    """
    Загружает данные из JSON-файла и создает объекты классов.
    :param file_path: Путь к JSON-файлу.
    :return: Список объектов класса Category.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    categories = []
    for category_data in data:
        products = []
        for product_data in category_data['products']:
            product = Product(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                quantity=product_data['quantity']
            )
            products.append(product)
        category = Category(
            name=category_data['name'],
            description=category_data['description'],
            products=products
        )
        categories.append(category)

    return categories
