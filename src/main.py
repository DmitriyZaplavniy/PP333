from .models import Product, Category
from .utils import load_data_from_json

if __name__ == "__main__":
    # Загрузка данных из JSON
    categories = load_data_from_json("products.json")

    # Вывод информации о категориях и товарах
    for category in categories:
        print(f"Категория: {category.name}")
        for product in category.products:
            print(f"  Товар: {product.name}, Цена: {product.price}, Количество: {product.quantity}")

    # Вывод общего количества категорий и товаров
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")
